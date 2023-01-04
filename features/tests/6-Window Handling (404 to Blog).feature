# Created by ababa at 8/8/2021
Feature: Tests for 404 page

  Scenario: User is able to navigate to Amazon blog from 404 page.
    Given Open Amazon product B07NF5WG11111111111111 page
    And Store original window
    When Click on a dog image
    And Switch to new window
    Then Verify blog is opened
    And Close blog
    And Return to original window

