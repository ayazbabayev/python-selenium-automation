# Created by ababa at 8/6/2021
Feature: Amazon Sign-In button: Visibility & Clickability

  Scenario: User can see & click on Amazon sign-in button
    Given User opens Amazon(No Sign In)
    Then Verify that Sign-In button is clickable
    When Wait for 8 seconds
    # If elements disappear before its' time,
    # Always verify like below (clickable)
    # before checking disappearance
    Then Verify that Sign-In button is clickable
    Then Verify that Sign-In button disappears