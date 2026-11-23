Feature: QR attendance for a course session
  As a student
  I want to record attendance by scanning a course QR code
  So that my attendance is recorded accurately

  Scenario: Successfully record attendance with a valid QR code
    Given a course session is open
    And the QR code belongs to student "2023001" and course "SET312"
    When the student scans the QR code
    Then the attendance record for "2023001" in "SET312" is saved

  Scenario: Reject an invalid or unrelated QR code
    Given a course session is open
    And the scanned QR code is invalid
    When the student scans the QR code
    Then the system rejects the attendance attempt
    And no attendance record is created

  Scenario: Do not record the same student's attendance twice
    Given a course session is open
    And student "2023001" is already marked present in "SET312"
    When the same student scans the QR code again
    Then the system reports that attendance is already recorded
    And only one attendance record exists for that student and session
