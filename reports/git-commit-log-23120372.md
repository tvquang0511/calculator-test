* commit 08237a0f2119fc1dcde40a578e096925882068db
| Author: tvquang0511 <23120346@student.hcmus.edu.vn>
| Date:   Mon Sep 28 15:31:45 2026 +0700
| 
|     generate 80 standard markdown test cases matching comprehensive test suite and excel design
| 
|  convert_excel_tc_to_markdown.py      | 139 +++++++++++++++++++++++++++++++++
|  tests/test-cases/build/TC-071.md     |  32 ++++++++
|  tests/test-cases/build/TC-072.md     |  31 ++++++++
|  tests/test-cases/build/TC-073.md     |  31 ++++++++
|  tests/test-cases/build/TC-074.md     |  30 +++++++
|  tests/test-cases/build/TC-075.md     |  26 ++++++
|  tests/test-cases/build/TC-076.md     |  31 ++++++++
|  tests/test-cases/build/TC-077.md     |  29 +++++++
|  tests/test-cases/build/TC-078.md     |  32 ++++++++
|  tests/test-cases/build/TC-079.md     |  26 ++++++
|  tests/test-cases/math/TC-001.md      |  34 ++++++++
|  tests/test-cases/math/TC-002.md      |  34 ++++++++
|  tests/test-cases/math/TC-003.md      |  34 ++++++++
|  tests/test-cases/math/TC-004.md      |  34 ++++++++
|  tests/test-cases/math/TC-005.md      |  33 ++++++++
|  tests/test-cases/math/TC-006.md      |  33 ++++++++
|  tests/test-cases/math/TC-007.md      |  33 ++++++++
|  tests/test-cases/math/TC-008.md      |  34 ++++++++
|  tests/test-cases/math/TC-009.md      |  34 ++++++++
|  tests/test-cases/math/TC-010.md      |  34 ++++++++
|  tests/test-cases/math/TC-011.md      |  33 ++++++++
|  tests/test-cases/math/TC-012.md      |  34 ++++++++
|  tests/test-cases/math/TC-013.md      |  34 ++++++++
|  tests/test-cases/math/TC-014.md      |  33 ++++++++
|  tests/test-cases/math/TC-015.md      |  33 ++++++++
|  tests/test-cases/math/TC-016.md      |  33 ++++++++
|  tests/test-cases/math/TC-017.md      |  33 ++++++++
|  tests/test-cases/math/TC-018.md      |  34 ++++++++
|  tests/test-cases/math/TC-019.md      |  33 ++++++++
|  tests/test-cases/math/TC-020.md      |  33 ++++++++
|  tests/test-cases/math/TC-021.md      |  33 ++++++++
|  tests/test-cases/math/TC-022.md      |  33 ++++++++
|  tests/test-cases/math/TC-023.md      |  33 ++++++++
|  tests/test-cases/math/TC-024.md      |  33 ++++++++
|  tests/test-cases/math/TC-025.md      |  33 ++++++++
|  tests/test-cases/math/TC-026.md      |  33 ++++++++
|  tests/test-cases/math/TC-027.md      |  33 ++++++++
|  tests/test-cases/math/TC-028.md      |  33 ++++++++
|  tests/test-cases/math/TC-029.md      |  34 ++++++++
|  tests/test-cases/math/TC-030.md      |  33 ++++++++
|  tests/test-cases/math/TC-031.md      |  34 ++++++++
|  tests/test-cases/math/TC-032.md      |  34 ++++++++
|  tests/test-cases/math/TC-033.md      |  34 ++++++++
|  tests/test-cases/math/TC-034.md      |  33 ++++++++
|  tests/test-cases/math/TC-035.md      |  33 ++++++++
|  tests/test-cases/math/TC-036.md      |  33 ++++++++
|  tests/test-cases/math/TC-037.md      |  33 ++++++++
|  tests/test-cases/math/TC-038.md      |  33 ++++++++
|  tests/test-cases/math/TC-039.md      |  33 ++++++++
|  tests/test-cases/math/TC-040.md      |  33 ++++++++
|  tests/test-cases/math/TC-041.md      |  33 ++++++++
|  tests/test-cases/math/TC-042.md      |  33 ++++++++
|  tests/test-cases/math/TC-MATH-001.md |  31 --------
|  tests/test-cases/math/TC-MATH-002.md |  30 -------
|  tests/test-cases/math/TC-MATH-003.md |  31 --------
|  tests/test-cases/math/TC-MATH-004.md |  30 -------
|  tests/test-cases/math/TC-MATH-005.md |  28 -------
|  tests/test-cases/str/TC-043.md       |  32 ++++++++
|  tests/test-cases/str/TC-044.md       |  32 ++++++++
|  tests/test-cases/str/TC-045.md       |  32 ++++++++
|  tests/test-cases/str/TC-046.md       |  32 ++++++++
|  tests/test-cases/str/TC-047.md       |  32 ++++++++
|  tests/test-cases/str/TC-048.md       |  32 ++++++++
|  tests/test-cases/str/TC-049.md       |  32 ++++++++
|  tests/test-cases/str/TC-050.md       |  32 ++++++++
|  tests/test-cases/str/TC-051.md       |  32 ++++++++
|  tests/test-cases/str/TC-052.md       |  32 ++++++++
|  tests/test-cases/str/TC-STR-001.md   |  30 -------
|  tests/test-cases/ui/TC-053.md        |  34 ++++++++
|  tests/test-cases/ui/TC-054.md        |  34 ++++++++
|  tests/test-cases/ui/TC-055.md        |  34 ++++++++
|  tests/test-cases/ui/TC-056.md        |  34 ++++++++
|  tests/test-cases/ui/TC-057.md        |  34 ++++++++
|  tests/test-cases/ui/TC-058.md        |  36 +++++++++
|  tests/test-cases/ui/TC-059.md        |  28 +++++++
|  tests/test-cases/ui/TC-060.md        |  28 +++++++
|  tests/test-cases/ui/TC-069.md        |  29 +++++++
|  tests/test-cases/ui/TC-070.md        |  28 +++++++
|  tests/test-cases/ui/TC-080.md        |  29 +++++++
|  tests/test-cases/ui/TC-UI-001.md     |  28 -------
|  tests/test-cases/ui/TC-UI-002.md     |  33 --------
|  tests/test-cases/ui/TC-UI-003.md     |  30 -------
|  tests/test-cases/val/TC-061.md       |  32 ++++++++
|  tests/test-cases/val/TC-062.md       |  32 ++++++++
|  tests/test-cases/val/TC-063.md       |  32 ++++++++
|  tests/test-cases/val/TC-064.md       |  32 ++++++++
|  tests/test-cases/val/TC-065.md       |  32 ++++++++
|  tests/test-cases/val/TC-066.md       |  32 ++++++++
|  tests/test-cases/val/TC-067.md       |  32 ++++++++
|  tests/test-cases/val/TC-068.md       |  26 ++++++
|  tests/test-cases/val/TC-VAL-001.md   |  30 -------
|  91 files changed, 2725 insertions(+), 301 deletions(-)
| 
* commit 98c93a39d96a3f0054f234bce507f7de736f6ede
| Author: tvquang0511 <23120346@student.hcmus.edu.vn>
| Date:   Mon Sep 28 15:26:46 2026 +0700
| 
|     fix timeout in TC-MATH-004 and handle disabled integerSelect in Build 4
| 
|  tests/calculator.spec.js                    | 138 ++++++++------------------
|  tests/comprehensive/pages/CalculatorPage.js |   3 +-
|  2 files changed, 46 insertions(+), 95 deletions(-)
| 
* commit c884d2e4764ffdda87b4bcc95f6860c06f209118
| Author: tinphan247 <tinphan111005@gmail.com>
| Date:   Mon Sep 28 15:23:26 2026 +0700
| 
|     add test_task, test_run issue templates and sprint-2-regression report
| 
|  .github/ISSUE_TEMPLATE/test_run.md     | 36 ++++++++++++++++++
|  .github/ISSUE_TEMPLATE/test_task.md    | 27 ++++++++++++++
|  tests/test-runs/sprint-2-regression.md | 63 ++++++++++++++++++++++++++++++++
|  3 files changed, 126 insertions(+)
| 
* commit 0f48137119fa0ceb6ff309fb2ce4c3fa1189a5d0
| Author: tinphan247 <tinphan111005@gmail.com>
| Date:   Mon Sep 28 15:12:20 2026 +0700
| 
|     add comprehensive 80 test cases suite with POM and test design excel
| 
|  .gitignore                                  |   10 +
|  Basic_Calculator_Test_Design.xlsx           |  Bin 0 -> 22922 bytes
|  export_test_cases_to_excel.py               | 1039 +++++++++++++++++++++++++
|  package-lock.json                           |   61 ++
|  package.json                                |    4 +
|  playwright.config.js                        |   12 +-
|  tests/comprehensive/calculator-80.spec.js   |  513 ++++++++++++
|  tests/comprehensive/pages/CalculatorPage.js |  166 ++++
|  8 files changed, 1802 insertions(+), 3 deletions(-)
| 
* commit c77acb5228f6a163ce58fbf3dc9d732d59adcc43
| Author: tvquang0511 <23120346@student.hcmus.edu.vn>
| Date:   Mon Sep 28 15:03:55 2026 +0700
| 
|     update test cases, bug reports, and traceability matrix to conform with GitHub QA standards
| 
|  .github/ISSUE_TEMPLATE/bug_report.md       | 35 ++++++++++++++++
|  .github/workflows/test.yml                 | 29 +++++++++++++
|  tests/bugs/BUG-01.md                       | 34 +++++++++++++++
|  tests/bugs/BUG-02.md                       | 34 +++++++++++++++
|  tests/bugs/BUG-03.md                       | 31 ++++++++++++++
|  tests/bugs/BUG-04.md                       | 31 ++++++++++++++
|  tests/bugs/BUG-05.md                       | 29 +++++++++++++
|  tests/bugs/BUG-06.md                       | 31 ++++++++++++++
|  tests/bugs/BUG-07.md                       | 30 +++++++++++++
|  tests/bugs/BUG-08.md                       | 31 ++++++++++++++
|  tests/bugs/BUG-09.md                       | 29 +++++++++++++
|  tests/test-cases/{ => math}/TC-MATH-001.md |  0
|  tests/test-cases/{ => math}/TC-MATH-002.md |  0
|  tests/test-cases/{ => math}/TC-MATH-003.md |  0
|  tests/test-cases/{ => math}/TC-MATH-004.md |  0
|  tests/test-cases/{ => math}/TC-MATH-005.md |  0
|  tests/test-cases/{ => str}/TC-STR-001.md   |  0
|  tests/test-cases/{ => ui}/TC-UI-001.md     |  0
|  tests/test-cases/{ => ui}/TC-UI-002.md     |  0
|  tests/test-cases/{ => ui}/TC-UI-003.md     |  0
|  tests/test-cases/{ => val}/TC-VAL-001.md   |  0
|  tests/test-runs/sprint-1-test-run.md       | 40 ++++++++++++++++++
|  tests/test-summary/traceability-matrix.md  | 63 ++++++++++++++++++++++++++++
|  23 files changed, 447 insertions(+)
| 
* commit ce0dac42cd2f26b92f7dbaef78e27cfe26dd3114
| Author: tvquang0511 <23120346@student.hcmus.edu.vn>
| Date:   Mon Sep 28 14:48:41 2026 +0700
| 
|     refactor test cases to follow standard template TC-[MODULE]-[NUMBER]
| 
|  03 - github_bug_management.pptx.pdf               | Bin 0 -> 194282 bytes
|  03 - github_testcase_management.pptx.pdf          | Bin 0 -> 418969 bytes
|  tests/calculator.spec.js                          |  90 +++----
|  tests/test-cases/TC-MATH-001.md                   |  31 +++
|  tests/test-cases/TC-MATH-002.md                   |  30 +++
|  tests/test-cases/TC-MATH-003.md                   |  31 +++
|  tests/test-cases/TC-MATH-004.md                   |  30 +++
|  tests/test-cases/TC-MATH-005.md                   |  28 +++
|  tests/test-cases/TC-STR-001.md                    |  30 +++
|  tests/test-cases/TC-UI-001.md                     |  28 +++
|  tests/test-cases/TC-UI-002.md                     |  33 +++
|  tests/test-cases/TC-UI-003.md                     |  30 +++
|  tests/test-cases/TC-VAL-001.md                    |  30 +++
|  tests/test-cases/TC01_UI_Elements_Availability.md |  34 ---
|  tests/test-cases/TC02_Addition_Operation.md       |  34 ---
|  tests/test-cases/TC03_Subtraction_Operation.md    |  34 ---
|  tests/test-cases/TC04_Division_Decimal_Result.md  |  36 ---
|  tests/test-cases/TC05_Division_By_Zero.md         |  32 ---
|  tests/test-cases/TC06_Concatenation_String.md     |  36 ---
|  tests/test-cases/TC07_Input_Validation_NaN.md     |  33 ---
|  tests/test-cases/TC08_Integers_Only_Checkbox.md   |  34 ---
|  .../test-cases/TC09_Clear_Button_Functionality.md |  31 ---
|  tests/test-cases/TC10_Consecutive_Calculations.md |  30 ---
|  tests/test-runner.js                              | 258 ++++++++++----------
|  tests/test-runs/test-run-report.md                |  44 ++--
|  tests/test-summary/test-summary-report.md         |  18 +-
|  26 files changed, 505 insertions(+), 540 deletions(-)
| 
* commit b2444947307fa2be6d2dc7191d04e44107c1b05c
| Author: tvquang0511 <23120346@student.hcmus.edu.vn>
| Date:   Mon Sep 28 14:39:57 2026 +0700
| 
|     remove redundant test-case folder
| 
|  tests/test-case/TC01_UI_Elements_Availability.md  | 34 -------------------
|  tests/test-case/TC02_Addition_Operation.md        | 34 -------------------
|  tests/test-case/TC03_Subtraction_Operation.md     | 34 -------------------
|  tests/test-case/TC04_Division_Decimal_Result.md   | 36 ---------------------
|  tests/test-case/TC05_Division_By_Zero.md          | 32 ------------------
|  tests/test-case/TC06_Concatenation_String.md      | 36 ---------------------
|  tests/test-case/TC07_Input_Validation_NaN.md      | 33 -------------------
|  tests/test-case/TC08_Integers_Only_Checkbox.md    | 34 -------------------
|  .../test-case/TC09_Clear_Button_Functionality.md  | 31 ------------------
|  tests/test-case/TC10_Consecutive_Calculations.md  | 30 -----------------
|  10 files changed, 334 deletions(-)
| 
* commit 7be1bcb44a2137a5d8ee501a095961963009247f
  Author: tvquang0511 <23120346@student.hcmus.edu.vn>
  Date:   Mon Sep 28 14:38:22 2026 +0700
  
      initial
  
   package.json                                      |  14 +
   playwright.config.js                              |  30 ++
   src/basicCalculator.html                          | 517 ++++++++++++++++++++
   tests/calculator.spec.js                          | 123 +++++
   tests/test-case/TC01_UI_Elements_Availability.md  |  34 ++
   tests/test-case/TC02_Addition_Operation.md        |  34 ++
   tests/test-case/TC03_Subtraction_Operation.md     |  34 ++
   tests/test-case/TC04_Division_Decimal_Result.md   |  36 ++
   tests/test-case/TC05_Division_By_Zero.md          |  32 ++
   tests/test-case/TC06_Concatenation_String.md      |  36 ++
   tests/test-case/TC07_Input_Validation_NaN.md      |  33 ++
   tests/test-case/TC08_Integers_Only_Checkbox.md    |  34 ++
   .../test-case/TC09_Clear_Button_Functionality.md  |  31 ++
   tests/test-case/TC10_Consecutive_Calculations.md  |  30 ++
   tests/test-cases/TC01_UI_Elements_Availability.md |  34 ++
   tests/test-cases/TC02_Addition_Operation.md       |  34 ++
   tests/test-cases/TC03_Subtraction_Operation.md    |  34 ++
   tests/test-cases/TC04_Division_Decimal_Result.md  |  36 ++
   tests/test-cases/TC05_Division_By_Zero.md         |  32 ++
   tests/test-cases/TC06_Concatenation_String.md     |  36 ++
   tests/test-cases/TC07_Input_Validation_NaN.md     |  33 ++
   tests/test-cases/TC08_Integers_Only_Checkbox.md   |  34 ++
   .../test-cases/TC09_Clear_Button_Functionality.md |  31 ++
   tests/test-cases/TC10_Consecutive_Calculations.md |  30 ++
   tests/test-runner.js                              | 380 ++++++++++++++
   tests/test-runs/test-run-report.md                |  61 +++
   tests/test-summary/test-summary-report.md         |  36 ++
   27 files changed, 1829 insertions(+)
