# Word Cloud

A word cloud displays words with sizes proportional to frequency or weight, providing a quick qualitative view of prominent terms.

## When to use it

- Use it for exploratory text summaries after cleaning and filtering common words.
- Avoid it when exact word counts, phrases, or sentiment need rigorous comparison.

## Jupyter notebook

Run the same commented example interactively in [word_cloud.ipynb](./word_cloud.ipynb).

## Python example

Install the required packages once:

```bash
python -m pip install matplotlib wordcloud
```

Save this as `word_cloud.py`, then run it. The example saves `word_cloud.png` in the current folder.

```python
import matplotlib.pyplot as plt
from wordcloud import STOPWORDS, WordCloud

# Supply cleaned text; remove irrelevant boilerplate in real data.
text = "fast reliable support simple dashboard helpful onboarding fast support analytics reporting reliable workflow simple integration support dashboard reporting fast onboarding analytics helpful workflow integration"

# Generate a cloud; stop words and collocations reduce visual noise.
cloud = WordCloud(width=1000, height=600, background_color="white", colormap="Blues", stopwords=STOPWORDS, collocations=False).generate(text)

# Draw, save, and display the word cloud.
fig, ax = plt.subplots(figsize=(10, 6))
ax.imshow(cloud, interpolation="bilinear")
ax.set_title("Common Terms in Customer Feedback", fontweight="bold")
ax.axis("off")
fig.tight_layout()
fig.savefig("word_cloud.png", dpi=200, bbox_inches="tight")
plt.show()
```

## Key choices

| Element | Recommendation |
| --- | --- |
| Purpose | Match the chart to the question the audience needs answered. |
| Labels | State the unit, time period, and measurement clearly. |
| Color | Use color sparingly and keep its meaning consistent. |
| Accessibility | Do not rely on color alone. |

