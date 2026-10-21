# Tips Dataset Analysis

## Research Question
Which factors — bill amount, party size, day of week, or meal time —
influence the tip a customer leaves at a restaurant?

## Dataset Source and Permissions
The `tips` dataset is bundled with the seaborn library and is publicly
available for analysis and teaching (BSD license). It contains 244
observations from a single restaurant. No personal, sensitive, or
restricted data is used in this project.

## Methods and Tools
- Python 3, pandas, seaborn, matplotlib, scikit-learn
- Exploratory data analysis with scatter and box plots
- Multiple linear regression using `total_bill` and `size` as predictors,
  evaluated on a 20% held-out test set (`random_state=42`)

## Key Findings
- **Total bill is the strongest single driver of tip amount.** The scatter
  plot (`figures/viz1_tip_vs_bill.png`) shows a clear positive, roughly
  linear relationship, with dinner bills generally higher than lunch bills.
- **Party size matters beyond the bill itself.** In the regression, the
  coefficient for `size` (0.265) is larger than for `total_bill` (0.091):
  holding the bill constant, each additional guest is associated with
  about $0.27 more in tip, while each extra dollar on the bill adds only
  about $0.09.
- **Tip amounts vary by day.** The box plot
  (`figures/viz2_tip_by_day.png`) shows the highest median tip on Sunday,
  though the spread is wide on every day.
- **Model fit:** R² ≈ 0.481 on the test set, meaning bill amount and party
  size together explain about 48% of the variation in tip amount.

## Limitation
The model explains only about half of the variance in tips, and the
dataset covers 244 parties from a single restaurant. Findings may not
generalize to other venues, regions, or time periods, and important
factors such as service quality are not captured in the data.

## How to Run
```bash
pip install -r requirements.txt
python analysis.py
