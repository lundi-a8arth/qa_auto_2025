import pytest


@pytest.mark.table_practice
def test_java_lang_filter(table_practice_page):
    table_practice_page.go_to()
    table_practice_page.press_radio_button_lang_java()
    visible_languages = table_practice_page.get_visible_languages()

    assert len(visible_languages) > 0, "No visible courses after filtering!"
    assert all(
        lang == "Java" for lang in visible_languages
    ), f"Expected only Java courses, but got: {visible_languages}"


@pytest.mark.table_practice
def test_beginner_lvl_filter(table_practice_page):
    table_practice_page.go_to()
    table_practice_page.checkbox_unselect_level_intermediate()
    table_practice_page.checkbox_unselect_level_advanced()
    visible_levels = table_practice_page.get_visible_levels()

    assert len(visible_levels) > 0
    assert all(
        level == "Beginner" for level in visible_levels
    ), f"Expected only Beginner courses, but got: {visible_levels}"


@pytest.mark.table_practice
def test_enrollments_filter(table_practice_page):
    table_practice_page.go_to()
    table_practice_page.dropdown_enroll_pick(10000)
    visible_enrollments = table_practice_page.get_visible_enrollments()

    assert len(visible_enrollments) > 0
    assert all(
        enrollment >= 10000 for enrollment in visible_enrollments
    ), f"Expected only courses with enrollment number >= 10000, but got: {visible_enrollments}"


@pytest.mark.table_practice
def test_combined_filters(table_practice_page):
    table_practice_page.go_to()
    table_practice_page.press_radio_button_lang_python()
    table_practice_page.checkbox_unselect_level_intermediate()
    table_practice_page.checkbox_unselect_level_advanced()
    table_practice_page.dropdown_enroll_pick(10000)
    visible_languages = table_practice_page.get_visible_languages()
    visible_levels = table_practice_page.get_visible_levels()
    visible_enrollments = table_practice_page.get_visible_enrollments()
    assert len(visible_languages) > 0
    assert len(visible_levels) > 0
    assert len(visible_enrollments) > 0
    assert all(
        lang == "Python" for lang in visible_languages
    ), f"Expected only Python courses, but got: {visible_languages}"
    assert all(
        level == "Beginner" for level in visible_levels
    ), f"Expected only Beginner courses, but got: {visible_levels}"
    assert all(
        enrollment >= 10000 for enrollment in visible_enrollments
    ), f"Expected only courses with enrollment number >= 10000, but got: {visible_enrollments}"


@pytest.mark.table_practice
def test_no_result_state(table_practice_page):
    table_practice_page.go_to()
    table_practice_page.press_radio_button_lang_python()
    table_practice_page.checkbox_unselect_level_beginner()
    assert table_practice_page.get_no_data_element()


@pytest.mark.table_practice
def test_reset_button(table_practice_page):
    table_practice_page.go_to()
    table_practice_page.checkbox_set_all(False)
    assert table_practice_page.get_reset_btn()
    table_practice_page.press_reset_btn()
    assert table_practice_page.get_selected_language() == "Any"
    assert table_practice_page.get_checked_levels() == [
        "Beginner",
        "Intermediate",
        "Advanced",
    ]
    assert table_practice_page.get_enrollments_option() == "Any"
    assert table_practice_page.check_reset_btn_is_invisible()
    assert table_practice_page.check_all_rows_visible()


@pytest.mark.table_practice
def test_sort_by_enrollments(table_practice_page):
    table_practice_page.go_to()
    table_practice_page.dropdown_sort_pick("Enrollments")
    values = table_practice_page.get_enrollments_values()
    sorted_values = sorted(values)

    assert values == sorted_values


@pytest.mark.table_practice
def test_sort_by_course_name(table_practice_page):
    table_practice_page.go_to()
    table_practice_page.dropdown_sort_pick("Course Name")
    values = table_practice_page.get_course_name_values()
    sorted_values = sorted(values)

    assert values == sorted_values
