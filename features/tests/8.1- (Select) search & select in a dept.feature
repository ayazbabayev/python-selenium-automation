# Created by ababa at 8/22/2022
Feature: Select feature: search & select in a department

  Scenario: User can search & select in a department
    Given open amazon page
    When Select department by alias industrial
    And Search for 3D Printer
    Then Verify industrial department is selected