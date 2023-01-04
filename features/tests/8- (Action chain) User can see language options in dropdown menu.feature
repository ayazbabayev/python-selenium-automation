# Created by ababa at 8/22/2021
Feature: Action chain: Dropdown menu.
  User can see language options.


  Scenario: User can see language options
    Given open amazon page
    When hover over language options
    Then verify spanish option present