Feature: Create a study group (S11, AP-16)
  As a student
  I want to create a study group
  So that I can invite my friends with a code

  Background:
    Given I am logged in as "sara@test.com"

  Scenario: Create a group and get an invite code
    When I create a group named "Agile study"
    Then the group is created
    And I receive a 6-character invite code

  Scenario: Group name is required
    When I create a group with an empty name
    Then I see the message "Group name is required"
    And no group is created

  Scenario: Two groups never share an invite code
    Given I have created a group named "Agile study"
    When I create a group named "Math revision"
    Then the two groups have different invite codes
