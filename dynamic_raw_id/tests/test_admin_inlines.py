"""
Test Dynamic Raw ID Widgets with Selenium in a ModelAdmin Inline
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from django.contrib.auth.models import User
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

if TYPE_CHECKING:
    from selenium.webdriver.firefox.webdriver import WebDriver


@pytest.mark.usefixtures("_add_page_with_inlines", "_sample_primary_keys")
def test_widgets(selenium: WebDriver) -> None:
    """
    Django Admin adds three 'inline' rows to the base model which we fill with
    three users.

    Then click the 'Add another' link three times, and fill another three users.
    """

    # Create six test users first
    for uid in range(6):
        test_value = f"inline{uid}"
        User.objects.create_user(username=test_value)

        # The inline form field starts with a zero index and is named
        # `lookup_id_modeltotestinlines_set-0-dynamic_raw_id_fk`

        # If this is the fourth user, click the 'Add another' link three times.
        if uid == 3:
            for _ in range(3):
                selenium.find_element(
                    By.LINK_TEXT, "Add another Model to test inlines"
                ).click()

        # Select the "Lookup" icon next to the field
        selenium.find_element(
            By.ID, f"lookup_id_modeltotestinlines_set-{uid}-dynamic_raw_id_fk"
        ).click()

        #  Activate the popup window with the `window.name = <window_id>`
        selenium.switch_to.window(selenium.window_handles[1])

        # Select the result element matching the link text
        WebDriverWait(selenium, 10).until(
            expected_conditions.element_to_be_clickable((By.LINK_TEXT, test_value))
        ).click()

        # Activate the default window
        selenium.switch_to.window(selenium.window_handles[0])

        # The label next to the field is filled in by an ajax call
        label = (
            By.ID,
            f"modeltotestinlines_set-{uid}-dynamic_raw_id_fk_dynamic_raw_id_label",
        )
        WebDriverWait(selenium, 10).until(
            expected_conditions.text_to_be_present_in_element(label, test_value)
        )
        assert selenium.find_element(*label).text == test_value
