# House Price EDA

An exploratory data analysis of residential property sales data, examining
what drives house prices and how features like square footage, bedroom
count, and condition relate to sale price.

This is my Week 4 portfolio project on a 12-month roadmap to become an
AI/ML Engineer. The original plan called for a Sydney-specific housing
dataset; I used a comparable house price dataset instead, covering the
same core EDA skills.

---

## Dataset

https://www.kaggle.com/code/hikmatullahmohammadi/house-price-prediction-eda-step-by-step

Residential property sales data including price, bedrooms, bathrooms,
square footage, condition, year built, year renovated, and location (city).

---

## Data Cleaning

- Inspected shape, column types, and checked for missing values
- Found rows with `price == 0`, which represent invalid or missing sale
  records rather than genuine $0 sales
- Considered imputing these values by grouping on `sqft_living` and using
  the group mean, but rejected this approach for two reasons:
  - Square footage is a near-continuous variable, so grouping by it
    produces mostly single-row groups — the resulting "average" isn't a
    meaningful estimate
  - Using square footage to fill in price would create circular reasoning,
    since a later part of the analysis specifically investigates the
    relationship between square footage and price
- Dropped the invalid rows instead, which is the more defensible choice
  for this kind of unambiguous data error

---

## Questions Explored

### 1. Does the number of bedrooms correlate with price?

A boxplot of price by bedroom count initially looked flat, which I first
read as "the dataset lacks price variety." Checking `price.describe()`
showed the real cause: a small number of very high-priced outliers
(upto $6M) were stretching the y-axis, compressing
the bulk of the data — which sits mostly between $500K and
$2M — into a thin band near the bottom of the chart.
Re-plotting by limiting y-axis to $2M revealed a clear upward trend in median price as bedroom count
increases.

**Correlation coefficient:** 0.2

### 2. Does square footage relate to price?

Visualized with a regression plot (`sns.regplot`) and computed the
correlation coefficient directly between `sqft_living` and `price`.
Most houses in the dataset fall between roughly 2,000 and 6,000 sqft.

**Correlation coefficient:** 0.43 — noticeably
higher than the bedroom correlation

### 3. How do all numeric variables relate to one another?

Built a correlation heatmap across all numeric columns
(`house_data.corr(numeric_only=True)` + `sns.heatmap`) to get an
at-a-glance view of every pairwise relationship at once.

Key takeaways:  There is a strong correlation between sqft_living and bedrooms, which is understandable as increase in the no of bedrooms will 
obviously increase the sqft. variables were most
strongly correlated with sqft_living

*Note: correlation heatmaps only capture linear relationships. A pair of
variables could have a strong non-linear relationship and still show a
correlation near zero, so this is a useful first pass rather than the
final word on every relationship in the data.*

---

## Visualizations

- **Regression plot** — price vs. year built
- **Histogram** — distribution of bedroom counts
- **Boxplot** — price by bedroom count, both on a linear scale (initially
  misleading due to outliers) and a log scale (clearer trend)
- **Correlation heatmap** — all numeric variables against each other

---

## Concepts Practiced

- Data cleaning and reasoning through why a value is likely invalid
  rather than genuinely meaningful (`price == 0`)
- Evaluating an imputation strategy and recognizing its flaws (data
  leakage risk, insufficient group size) before applying it
- Pandas `groupby()` with single and multiple columns, both raw and
  aggregated
- Choosing appropriate plot types for discrete vs. continuous variables
- Diagnosing a misleading chart (squished boxplot) by checking summary
  statistics and applying a log scale, rather than misreading it as a
  property of the underlying data
- Building and interpreting a correlation heatmap across multiple variables

---

## What I Learned

The biggest lesson from this project was that a chart that looks "flat"
or "boring" is often a sign that something about the visualization needs
adjusting — not that the underlying data lacks variety. My initial boxplot
of price by bedroom count looked squished, and my first instinct was to
conclude the dataset itself was limited. Checking `.describe()` showed a
small number of extreme high-price outliers were stretching the axis and
compressing everything else. Switching to a log scale revealed a much
clearer pattern that was there all along.

I also learned to be more careful about how I test a question like
"is there a correlation between X and Y." My first pass at the bedrooms
question used an ungrouped `apply()` that just listed raw values with no
aggregation — which can't actually answer the question. Reaching for
`.corr()` or a proper `groupby().mean()` aggregation is now my default
starting point whenever I want to check a relationship between two
variables, rather than relying on a first visual impression.

[Add 1-2 more sentences in your own words]

---

## What's Next

Moving into Phase 2 of the roadmap: a math refresh (linear algebra,
calculus, and statistics) followed by classical machine learning with
scikit-learn, starting with an end-to-end ML project and regression models.

---

*Week 4 portfolio project — 12-month AI/ML Engineer roadmap, June 2026*