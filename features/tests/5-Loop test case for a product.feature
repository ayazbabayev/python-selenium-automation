# Created by ababa at 8/1/2021
Feature: Loop test for a product

  Scenario: User can select colors of a product in Amazon
    Given Amazon page for product B08LYZMF86
    Then Verify user can click shown colors
    