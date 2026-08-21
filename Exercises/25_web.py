#Projekt – Kursprogram: Bygg ett program för en person som läser kurser.
#Programmet ska kunna: - Lägga till kurs
#- Beräkna timmar per vecka
#- Visa alla kurser
#- Beräkna total studietid
#- Söka kurs
#- Ändra studietakt
#- Ta bort kurs
#Föreslagna funktioner: add_course(), calc_study_hours(), show_courses(), calc_total_hours(), find_course(), remove_course(),update_rate(), save_courses(), load_courses(), run_menu()
#Challenge: Skapa en meny med alternativ för att lägga till, visa, söka, ändra, ta bort och avsluta.

import streamlit as st
from supabase import create_client



# --------------------------------------------------
# Inställningar
# --------------------------------------------------

st.set_page_config(
    page_title="Kursplanerare",
    page_icon="📚",
    layout="wide"
)

supabase = create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_KEY"]
)


# --------------------------------------------------
# Funktioner
# --------------------------------------------------

def calc_study_hours(rate):
    return rate * 40 / 100

def add_course_to_database(course):
    response = (
        supabase
        .table("courses")
        .insert(course)
        .execute()
    )

    return response.data[0]


def update_course_in_database(course_id, rate):
    hours = calc_study_hours(rate)

    response = (
        supabase
        .table("courses")
        .update({
            "rate": rate,
            "hours": hours
        })
        .eq("id", course_id)
        .execute()
    )

    return response

def delete_course_from_database(course_id):
    response = (
        supabase
        .table("courses")
        .delete()
        .eq("id", course_id)
        .execute()
    )

    return response


def calc_total_hours(courses):
    total_hours = 0

    for course in courses:
        total_hours += course["hours"]

    return total_hours


def load_courses():
    response = supabase.table("courses").select("*").execute()
    return response.data




# --------------------------------------------------
# Session state
# --------------------------------------------------

if "courses" not in st.session_state:
    st.session_state.courses = load_courses()


# --------------------------------------------------
# Rubrik
# --------------------------------------------------

st.title("📚 Mitt kursprogram")

st.write(
    "Planera och följ upp dina fristående högskolekurser."
)

st.divider()


# --------------------------------------------------
# Sammanfattning
# --------------------------------------------------

total_hours = calc_total_hours(st.session_state.courses)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Antal kurser",
        len(st.session_state.courses)
    )

with col2:
    total_points = sum(
        course["points"]
        for course in st.session_state.courses
    )

    st.metric(
        "Totalt HP",
        f"{total_points:.1f}"
    )

with col3:
    st.metric(
        "Studietid / vecka",
        f"{total_hours:.1f} h"
    )


st.divider()


# --------------------------------------------------
# Lägg till kurs
# --------------------------------------------------

st.header("➕ Lägg till kurs")

col1, col2 = st.columns(2)

with col1:

    name = st.text_input(
        "Namn",
        placeholder="Exempel: Hans"
    )

    course = st.text_input(
        "Kurs",
        placeholder="Exempel: Python och AI"
    )

with col2:

    points = st.number_input(
        "Högskolepoäng",
        min_value=0.0,
        step=0.5,
        value=7.5
    )

    rate = st.number_input(
        "Studietakt (%)",
        min_value=0,
        max_value=100,
        step=10,
        value=50
    )


hours = calc_study_hours(rate)

st.info(
    f"Studietakten {rate} % motsvarar "
    f"**{hours:.1f} timmar per vecka**."
)


if st.button(
    "➕ Lägg till kurs",
    type="primary",
    use_container_width=True
):

    if not course:
        st.warning("Ange ett kursnamn.")

    else:

        course_info = {
            "name": name,
            "course": course,
            "points": points,
            "rate": rate,
            "hours": hours
        }

        saved_course = add_course_to_database(course_info)

        st.session_state.courses.append(saved_course)

        st.success(
            f"{course} har registrerats!"
        )

        st.rerun()


st.divider()


# --------------------------------------------------
# Mina kurser
# --------------------------------------------------

st.header("📋 Mina kurser")


if st.session_state.courses:

    table_data = []

    for course in st.session_state.courses:

        table_data.append({
            "Namn": course["name"],
            "Kurs": course["course"],
            "HP": course["points"],
            "Studietakt": f'{course["rate"]} %',
            "Tid / vecka": f'{course["hours"]:.1f} h'
        })

    st.dataframe(
        table_data,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info(
        "Du har ännu inte registrerat någon kurs."
    )


st.divider()


# --------------------------------------------------
# Sök kurs
# --------------------------------------------------

st.header("🔎 Sök kurs")

search = st.text_input(
    "Sök efter kurs",
    placeholder="Skriv exempelvis Python eller AI"
)


if search:

    found_courses = []

    for course in st.session_state.courses:

        if search.lower() in course["course"].lower():
            found_courses.append(course)

    if found_courses:

        for course in found_courses:

            st.success(
                f'**{course["course"]}** — '
                f'{course["points"]} hp — '
                f'{course["rate"]} % — '
                f'{course["hours"]:.1f} h/vecka'
            )

    else:

        st.warning(
            "Ingen kurs matchade din sökning."
        )


st.divider()


# --------------------------------------------------
# Ändra studietakt
# --------------------------------------------------

st.header("✏️ Ändra studietakt")


if st.session_state.courses:

    course_names = [
        course["course"]
        for course in st.session_state.courses
    ]

    col1, col2 = st.columns(2)

    with col1:

        selected_course = st.selectbox(
            "Välj kurs",
            course_names,
            key="update_course"
        )

    with col2:

        new_rate = st.number_input(
            "Ny studietakt (%)",
            min_value=0,
            max_value=100,
            step=10,
            key="new_rate"
        )


if st.button(
    "✏️ Ändra studietakt",
    use_container_width=True
):

    for course in st.session_state.courses:

        if course["course"] == selected_course:

            response = update_course_in_database(
                course["id"],
                new_rate
            )

            if response.data:

                course["rate"] = new_rate
                course["hours"] = calc_study_hours(new_rate)

                st.success(
                    f"{selected_course} är ändrad till "
                    f"{new_rate} %."
                )

                st.rerun()

            else:

                st.error(
                    f"Kunde inte uppdatera kursen med "
                    f"ID {course['id']}."
                )

else:

    st.info("Lägg till en kurs först.")


st.divider()


# --------------------------------------------------
# Ta bort kurs
# --------------------------------------------------

st.header("🗑️ Ta bort kurs")


if st.session_state.courses:

    course_names = [
        course["course"]
        for course in st.session_state.courses
    ]

    selected_course = st.selectbox(
        "Välj kurs att ta bort",
        course_names,
        key="remove_course"
    )

    if st.button(
        "🗑️ Ta bort kurs",
        use_container_width=True
    ):

        for course in st.session_state.courses:

            if course["course"] == selected_course:

                response = delete_course_from_database(
                    course["id"]
                )

                if response.data:

                    st.session_state.courses.remove(course)

                    st.success(
                        f"{selected_course} har tagits bort."
                    )

                    st.rerun()

                else:

                    st.error(
                        f"Kunde inte ta bort kursen "
                        f"med ID {course['id']}."
                    )

else:

    st.info("Det finns inga kurser att ta bort.")

# --------------------------------------------------
# Total
# --------------------------------------------------

st.subheader("⏱️ Total studietid")

st.metric(
    "Studietid per vecka",
    f"{calc_total_hours(st.session_state.courses):.1f} timmar"
)