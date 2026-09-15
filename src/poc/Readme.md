# POC

## Statistical & Distribution Charts

```Shell
% streamlit run  src/poc/main.py
```

# JSON report merge builder

Run this from this folder:

```bash
python3 src/poc/utils/json_merge.py
```

It reads `config/masterreport.json`, resolves every `$include` relative to the file declaring it, validates the final artifact, and creates `config/reports.json`. Final validation requires non-empty `application`, `version`, `chartId`, `dataAdapter.modulePath`, `dataAdapter.className`, and `dataAdapter.method` fields, plus an object-valued `dataAdapter.parameters` field. The output is also checked for strict JSON serializability before it is written.

The first occurrence of a `chartId` establishes its position. A later occurrence replaces that chart and prints a warning. Pass explicit paths when needed:

```bash
python src/poc/utils/json_merge.py path/to/masterreport.json path/to/reports.json
```

## TODO Charts

* **Categorical**
  * **Vertical Bar ✓**
  * **Horizontal Bar ✓**
  * **Stacked Bar ✓**
  * **Grouped Bar ✓**
  * **Lollipop ✓**
  * **Radar Chart ✓**
* **Distributional**
  * **Histogram ✓**
  * **Box ✓**
  * **Violin ✓**
  * **Density  (KDE) ✓**
  * **Strip / Swarm ✓**
  * **Error Bar ✓**
* **GEO Spatial**
  * **Choropleth Map ✓**
  * **Scatter Map / Dot Map ✓**
  * **Connection Map ✓**
* **Matrix & Relationship**
  * **Heatmap ✓**
  * **Clustermap✓**
  * **Sankey Diagram ✓**
  * **Chord Diagram✓**
* **Part-to-Whole & Hierarchical**
  * **Pie✓**
  * **Donut ✓**
  * **Treemap ✓**
  * **Sunburst**
* **Relational & Trend**
  * **Line Chart ✓**
  * **Scatter Plot ✓**
  * **Bubble Chart**
  * **Connected Scatter**
  * **Area Chart**
  * **Stacked Area Chart**
* **3D & Advanced Technical Charts**
  * **Scatter Plot ✓**
  * **Surface Plot✓**
  * **Parallel Coordinates Plot✓**
  * **Word Cloud✓**
* **Financial**
  * **Market Analysis ✓**

## Available Charts

# Charts

## 📂 Hierarchy

<!-- PDF_LIST_START -->

* 📁 **3D**
  * 📄 [3D Parallel Cordinates Interactive](<../../reports/3D/3D%20Parallel%20Cordinates_interactive.pdf>)
  * 📄 [3D Parallel Cordinates Static](<../../reports/3D/3D%20Parallel%20Cordinates_static.pdf>)
  * 📄 [3D Scatter Interactive](<../../reports/3D/3D%20Scatter_interactive.pdf>)
  * 📄 [3D Scatter Static](<../../reports/3D/3D%20Scatter_static.pdf>)
  * 📄 [3D Surface Interactive](<../../reports/3D/3D%20Surface_interactive.pdf>)
  * 📄 [3D Surface Static](<../../reports/3D/3D%20Surface_static.pdf>)
  * 📄 [3D Word Cloud Interactive](<../../reports/3D/3D%20Word%20Cloud_interactive.pdf>)
  * 📄 [3D Word Cloud Static](<../../reports/3D/3D%20Word%20Cloud_static.pdf>)
* 📁 **Categorical**
  * 📄 [Bar Chart Interactive](<../../reports/Categorical/Bar%20Chart_interactive.pdf>)
  * 📄 [Bar Chart Static](<../../reports/Categorical/Bar%20Chart_static.pdf>)
  * 📄 [Grouped Bar Sales Interactive](<../../reports/Categorical/Grouped%20Bar%20Sales_interactive.pdf>)
  * 📄 [Grouped Bar Sales Static](<../../reports/Categorical/Grouped%20Bar%20Sales_static.pdf>)
  * 📄 [Lollipop Chart Interactive](<../../reports/Categorical/Lollipop%20Chart_interactive.pdf>)
  * 📄 [Lollipop Chart Static](<../../reports/Categorical/Lollipop%20Chart_static.pdf>)
  * 📄 [Product Horizontal Bar Chart Interactive](<../../reports/Categorical/Product%20Horizontal%20Bar%20Chart_interactive.pdf>)
  * 📄 [Product Horizontal Bar Chart Static](<../../reports/Categorical/Product%20Horizontal%20Bar%20Chart_static.pdf>)
  * 📄 [Product Verttical Bar Chart Interactive](<../../reports/Categorical/Product%20Verttical%20Bar%20Chart_interactive.pdf>)
  * 📄 [Product Verttical Bar Chart Static](<../../reports/Categorical/Product%20Verttical%20Bar%20Chart_static.pdf>)
  * 📄 [Radar Chart Interactive](<../../reports/Categorical/Radar%20Chart_interactive.pdf>)
  * 📄 [Radar Chart Static](<../../reports/Categorical/Radar%20Chart_static.pdf>)
  * 📄 [Stacked Bar Chart Interactive](<../../reports/Categorical/Stacked%20Bar%20Chart_interactive.pdf>)
  * 📄 [Stacked Bar Chart Static](<../../reports/Categorical/Stacked%20Bar%20Chart_static.pdf>)
  * 📄 [Stsacked Bar Chart Interactive](<../../reports/Categorical/Stsacked%20Bar%20Chart_interactive.pdf>)
  * 📄 [Stsacked Bar Chart Static](<../../reports/Categorical/Stsacked%20Bar%20Chart_static.pdf>)
* 📁 **Distribution**
  * 📄 [1 Histogram Interactive](../../reports/Distribution/1_histogram_interactive.pdf)
  * 📄 [1 Histogram Static](../../reports/Distribution/1_histogram_static.pdf)
  * 📄 [2 Boxplot Interactive](../../reports/Distribution/2_boxplot_interactive.pdf)
  * 📄 [2 Boxplot Static](../../reports/Distribution/2_boxplot_static.pdf)
  * 📄 [3 Violinplot Interactive](../../reports/Distribution/3_violinplot_interactive.pdf)
  * 📄 [3 Violinplot Static](../../reports/Distribution/3_violinplot_static.pdf)
  * 📄 [4 Density Interactive](../../reports/Distribution/4_density_interactive.pdf)
  * 📄 [4 Density Static](../../reports/Distribution/4_density_static.pdf)
  * 📄 [5 Stripplot Interactive](../../reports/Distribution/5_stripplot_interactive.pdf)
  * 📄 [5 Stripplot Static](../../reports/Distribution/5_stripplot_static.pdf)
  * 📄 [6 Errorbar Interactive](../../reports/Distribution/6_errorbar_interactive.pdf)
  * 📄 [6 Errorbar Static](../../reports/Distribution/6_errorbar_static.pdf)
* 📁 **Financial**
  * 📄 [Market Analysis Of ^Nsei 1Wk 4Mo Interactive](<../../reports/Financial/Market%20Analysis%20of%20%5ENSEI_1wk_4mo_interactive.pdf>)
* 📁 **Geo Spatial**
  * 📄 [Global Interactive Connection Map With Economic Data Interactive](<../../reports/Geo_Spatial/Global%20Interactive%20Connection%20Map%20with%20Economic%20Data_interactive.pdf>)
  * 📄 [Scatter Map Or Geo Plot Interactive](<../../reports/Geo_Spatial/Scatter%20Map%20or%20Geo-Plot_interactive.pdf>)
  * 📄 [Scatter Map Or Geo Plot Static](<../../reports/Geo_Spatial/Scatter%20Map%20or%20Geo-Plot_static.pdf>)
* 📁 **Matrix And Relationship**
  * 📄 [Chord Diagram Interactive](<../../reports/Matrix_And_Relationship/Chord%20Diagram_interactive.pdf>)
  * 📄 [Chord Diagram Static](<../../reports/Matrix_And_Relationship/Chord%20Diagram_static.pdf>)
  * 📄 [Heatmap Interactive](../../reports/Matrix_And_Relationship/HeatMap_interactive.pdf)
  * 📄 [Heatmap Static](../../reports/Matrix_And_Relationship/HeatMap_static.pdf)
  * 📄 [Interactive Plotly Clustergram Interactive](<../../reports/Matrix_And_Relationship/Interactive%20Plotly%20Clustergram_interactive.pdf>)
  * 📄 [Interactive Plotly Clustergram Static](<../../reports/Matrix_And_Relationship/Interactive%20Plotly%20Clustergram_static.pdf>)
  * 📄 [Plotly Sankey Interactive](<../../reports/Matrix_And_Relationship/Plotly%20Sankey_interactive.pdf>)
  * 📄 [Plotly Sankey Static](<../../reports/Matrix_And_Relationship/Plotly%20Sankey_static.pdf>)
* 📁 **Part To Whole**
  * 📄 [Donut Chart Interactive](<../../reports/Part-To-Whole/Donut%20Chart_interactive.pdf>)
  * 📄 [Donut Chart Static](<../../reports/Part-To-Whole/Donut%20Chart_static.pdf>)
  * 📄 [Tree Map Interactive](<../../reports/Part-To-Whole/Tree%20Map_interactive.pdf>)
  * 📄 [Tree Map Static](<../../reports/Part-To-Whole/Tree%20Map_static.pdf>)
* 📁 **Relational**
  * 📄 [Line Chart Interactive](<../../reports/Relational/Line%20Chart_interactive.pdf>)
  * 📄 [Line Chart Static](<../../reports/Relational/Line%20Chart_static.pdf>)
  * 📄 [Scatter Plot Interactive](<../../reports/Relational/Scatter%20Plot_interactive.pdf>)
  * 📄 [Scatter Plot Static](<../../reports/Relational/Scatter%20Plot_static.pdf>)

<!-- PDF_LIST_END -->
