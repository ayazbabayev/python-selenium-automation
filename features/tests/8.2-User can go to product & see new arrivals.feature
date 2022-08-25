# Created by ababa at 8/24/2022
Feature: Dropdown menu test for new arrivals.
    User can see new arrivals.

  Scenario: User can go to product & see new arrivals
    Given User goes to product B074TBCSC8 on Amazon
    When Hovers over new arrivals
    Then Verify that user sees 6 deals in new arrivals tab
