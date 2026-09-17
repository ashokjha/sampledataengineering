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

## Charts

### 1. Categorical

  1.1 [Vertical Bar](../docs/categorical/Vertical_bar_README.md)  -> [see](../docs/categorical/vertical_bar.ipynb) 
  1.2 [Horizontal Bar](../docs/categorical/Horizontal_bar_README.md)  -> [see](../docs/categorical/horizontal_bar.ipynb) 
  1.3 [Stacked Bar](../docs/categorical/Stacked_bar_README.md)  -> [see](../docs/categorical/stacked_bar.ipynb) 
  1.4 [Grouped Bar](../docs/categorical/Grouped_bar_README.md)  -> [see](../docs/categorical/grouped_bar.ipynb) 
  1.5 [Lollipop](../docs/categorical/Lollipop_README.md)  -> [see](../docs/categorical/lollipop.ipynb) 
  1.6 [Radar Chart](../docs/categorical/Radar_chart_README.md)  -> [see](../docs/categorical/radar_chart.ipynb)

### 2. Distributional

  2.1 [Histogram](../docs/distribution/Histogram_README.md)  -> [see](../docs/distribution/histogram.ipynb) 
  2.2 [Box](../docs/distribution/Box_plot_README.md)  -> [see](../docs/distribution/box_plot.ipynb) 
  2.3 [Violin](../docs/distribution/Violin_plot_README.md)  -> [see](../docs/distribution/violin_plot.ipynb) 
  2.4 [Density (KDE)](../docs/distribution/Density_plot_kde_README.md)  -> [see](../docs/distribution/density_plot_kde.ipynb) 
  2.5 [Strip / Swarm](../docs/distribution/StrpSwarn_README.md)  -> [see](../docs/distribution/strip_swarm_plot.ipynb) 
  2.6 [Error Bar](../docs/distribution/Error_bar_README.md)  -> [see](../docs/distribution/error_bar_chart.ipynb)

### 3. Spatial

  3.1 [Choropleth Map](../docs/geo/Choropleth_README.md)  -> [see](../docs/geo/choropleth_map.ipynb) 
  3.2 [Scatter Map / Dot Map](../docs/geo/ScatterOrDot_map_README.md)  -> [see](../docs/geo/scatter_map_dot_map.ipynb)
  3.3 [Connection Map](../docs/geo/Connection_map_README.md) and [Check](../docs/geo/connection_map.ipynb)

### 4.Matrix & Relationship

  4.1 [Heatmap](../docs/matrix/HeatMap_README.md)  -> [see](../docs/matrix/heatmap.ipynb)
  4.2 [Clustermap](../docs/matrix/Clustermap_README.md)  -> [see](../docs/matrix/clustermap.ipynb)
  4.3 [Sankey Diagram](../docs/matrix/Sankey_Diagram_README.md) -> [see](../docs/matrix/sankey_diagram.ipynb)
  4.4 [Chord Diagram](../docs/matrix/Chord_Diagram_README.md)  -> [see](../docs/matrix/chord_diagram.ipynb)

### 5. Part-to-Whole & Hierarchical

  5.1 [Pie](../docs/p2w/Pie_README.md)  -> [see](../docs/p2w/pie_chart.ipynb)
  5.2 [Donut](../docs/p2w/Donut_README.md)  -> [see](../docs/p2w/donut_chart.ipynb)
  5.3 [Treemap](../docs/p2w/Treemap_README.md)  -> [see](../docs/p2w/treemap.ipynb)
  5.4 [Sunburst](../docs/p2w/Sunburst_README.md)  -> [see](../docs/p2w/sunburst.ipynb)

### 6. Relational & Trend

  6.1 [Line Chart](../docs/relation/Line_chart_README.md)  -> [see](../docs/relation/line_chart.ipynb)
  6.2 [Scatter Plot](../docs/relation/Scatter_plot_README.md)  -> [see](../docs/relation/scatter_plot.ipynb)
  6.3 [Bubble Chart](../docs/relation/Bubble_Chart_README.md)  -> [see](../docs/relation/bubble_chart.ipynb)
  6.4 [Connected Scatter](<../docs/relation/Connected%20Scatter_README.md>)  -> [see](../docs/relation/connected_scatter.ipynb)
  6.5 [Area Chart](../docs/relation/Area_Chart_README.md)  -> [see](../docs/relation/area_chart.ipynb)
  6.6 [Stacked Area Chart](../docs/relation/Stacked_Area_Chart_README.md)  -> [see](../docs/relation/stacked_area_chart.ipynb)

### 7. 3D & Advanced Technical Charts

  7.1 [Scatter Plot](../docs/threed/Scatter_plot_3D_README.md)  -> [see](../docs/threed/scatter_plot_3d.ipynb)
  7.2 [Surface Plot](../docs/threed/Surface_Plot_README.md)  -> [see](../docs/threed/scatter_surface_plot.ipynb)
  7.3 [Parallel Coordinates Plot](../docs/threed/Parallel_Coordinates_Plot_README.md)  -> [see](../docs/threed/parallel_coordinates_plot.ipynb)
  7.4 [Word Cloud](../docs/threed/Word_cloud_README.md)  -> [see](../docs/threed/word_cloud.ipynb)

### 8. Financial

  8.1 Market Analysis

# Charts PDF

## 📂 Hierarchy

<!-- PDF_LIST_START -->
* 📁 **3D**
  * 📄 [3D Parallel Cordinates Interactive](../../reports/3D/3D%20Parallel%20Cordinates_interactive.pdf)
  * 📄 [3D Parallel Cordinates Static](../../reports/3D/3D%20Parallel%20Cordinates_static.pdf)
  * 📄 [3D Scatter Interactive](../../reports/3D/3D%20Scatter_interactive.pdf)
  * 📄 [3D Scatter Static](../../reports/3D/3D%20Scatter_static.pdf)
  * 📄 [3D Surface Interactive](../../reports/3D/3D%20Surface_interactive.pdf)
  * 📄 [3D Surface Static](../../reports/3D/3D%20Surface_static.pdf)
  * 📄 [3D Word Cloud Interactive](../../reports/3D/3D%20Word%20Cloud_interactive.pdf)
  * 📄 [3D Word Cloud Static](../../reports/3D/3D%20Word%20Cloud_static.pdf)
* 📁 **Categorical**
  * 📄 [Bar Chart Interactive](../../reports/Categorical/Bar%20Chart_interactive.pdf)
  * 📄 [Bar Chart Static](../../reports/Categorical/Bar%20Chart_static.pdf)
  * 📄 [Grouped Bar Sales Interactive](../../reports/Categorical/Grouped%20Bar%20Sales_interactive.pdf)
  * 📄 [Grouped Bar Sales Static](../../reports/Categorical/Grouped%20Bar%20Sales_static.pdf)
  * 📄 [Lollipop Chart Interactive](../../reports/Categorical/Lollipop%20Chart_interactive.pdf)
  * 📄 [Lollipop Chart Static](../../reports/Categorical/Lollipop%20Chart_static.pdf)
  * 📄 [Product Horizontal Bar Chart Interactive](../../reports/Categorical/Product%20Horizontal%20Bar%20Chart_interactive.pdf)
  * 📄 [Product Horizontal Bar Chart Static](../../reports/Categorical/Product%20Horizontal%20Bar%20Chart_static.pdf)
  * 📄 [Product Verttical Bar Chart Interactive](../../reports/Categorical/Product%20Verttical%20Bar%20Chart_interactive.pdf)
  * 📄 [Product Verttical Bar Chart Static](../../reports/Categorical/Product%20Verttical%20Bar%20Chart_static.pdf)
  * 📄 [Radar Chart Interactive](../../reports/Categorical/Radar%20Chart_interactive.pdf)
  * 📄 [Radar Chart Static](../../reports/Categorical/Radar%20Chart_static.pdf)
  * 📄 [Stacked Bar Chart Interactive](../../reports/Categorical/Stacked%20Bar%20Chart_interactive.pdf)
  * 📄 [Stacked Bar Chart Static](../../reports/Categorical/Stacked%20Bar%20Chart_static.pdf)
  * 📄 [Stsacked Bar Chart Interactive](../../reports/Categorical/Stsacked%20Bar%20Chart_interactive.pdf)
  * 📄 [Stsacked Bar Chart Static](../../reports/Categorical/Stsacked%20Bar%20Chart_static.pdf)
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
  * 📄 [Market Analysis Of ^Nsei 1Wk 4Mo Interactive](../../reports/Financial/Market%20Analysis%20of%20%5ENSEI_1wk_4mo_interactive.pdf)
* 📁 **Geo Spatial**
  * 📄 [Global Interactive Connection Map With Economic Data Interactive](../../reports/Geo_Spatial/Global%20Interactive%20Connection%20Map%20with%20Economic%20Data_interactive.pdf)
  * 📄 [Scatter Map Or Geo Plot Interactive](../../reports/Geo_Spatial/Scatter%20Map%20or%20Geo-Plot_interactive.pdf)
  * 📄 [Scatter Map Or Geo Plot Static](../../reports/Geo_Spatial/Scatter%20Map%20or%20Geo-Plot_static.pdf)
* 📁 **Matrix And Relationship**
  * 📄 [Chord Diagram Interactive](../../reports/Matrix_And_Relationship/Chord%20Diagram_interactive.pdf)
  * 📄 [Chord Diagram Static](../../reports/Matrix_And_Relationship/Chord%20Diagram_static.pdf)
  * 📄 [Heatmap Interactive](../../reports/Matrix_And_Relationship/HeatMap_interactive.pdf)
  * 📄 [Heatmap Static](../../reports/Matrix_And_Relationship/HeatMap_static.pdf)
  * 📄 [Interactive Plotly Clustergram Interactive](../../reports/Matrix_And_Relationship/Interactive%20Plotly%20Clustergram_interactive.pdf)
  * 📄 [Interactive Plotly Clustergram Static](../../reports/Matrix_And_Relationship/Interactive%20Plotly%20Clustergram_static.pdf)
  * 📄 [Plotly Sankey Interactive](../../reports/Matrix_And_Relationship/Plotly%20Sankey_interactive.pdf)
  * 📄 [Plotly Sankey Static](../../reports/Matrix_And_Relationship/Plotly%20Sankey_static.pdf)
* 📁 **Part To Whole**
  * 📄 [Donut Chart Interactive](../../reports/Part-To-Whole/Donut%20Chart_interactive.pdf)
  * 📄 [Donut Chart Static](../../reports/Part-To-Whole/Donut%20Chart_static.pdf)
  * 📄 [Pie Chart Interactive](../../reports/Part-To-Whole/Pie%20Chart_interactive.pdf)
  * 📄 [Pie Chart Static](../../reports/Part-To-Whole/Pie%20Chart_static.pdf)
  * 📄 [Sun Burst Chart Interactive](../../reports/Part-To-Whole/Sun%20Burst%20Chart_interactive.pdf)
  * 📄 [Sun Burst Chart Static](../../reports/Part-To-Whole/Sun%20Burst%20Chart_static.pdf)
  * 📄 [Tree Map Interactive](../../reports/Part-To-Whole/Tree%20Map_interactive.pdf)
  * 📄 [Tree Map Static](../../reports/Part-To-Whole/Tree%20Map_static.pdf)
* 📁 **Relational**
  * 📄 [Bubble Chart Interactive](../../reports/Relational/Bubble%20Chart_interactive.pdf)
  * 📄 [Bubble Chart Static](../../reports/Relational/Bubble%20Chart_static.pdf)
  * 📄 [Company Revenue Stream Breakdown (2024   2026) Stacked Area Chart Interactive](../../reports/Relational/Company%20Revenue%20Stream%20Breakdown%20%282024%20-%202026%29%20Stacked%20Area%20Chart_interactive.pdf)
  * 📄 [Company Revenue Stream Breakdown (2024   2026) Stacked Area Chart Static](../../reports/Relational/Company%20Revenue%20Stream%20Breakdown%20%282024%20-%202026%29%20Stacked%20Area%20Chart_static.pdf)
  * 📄 [Line Chart Interactive](../../reports/Relational/Line%20Chart_interactive.pdf)
  * 📄 [Line Chart Static](../../reports/Relational/Line%20Chart_static.pdf)
  * 📄 [Monthly Growth Projection Connected Scatter Plot Interactive](../../reports/Relational/Monthly%20Growth%20Projection%20Connected%20Scatter%20plot_interactive.pdf)
  * 📄 [Monthly Growth Projection Connected Scatter Plot Static](../../reports/Relational/Monthly%20Growth%20Projection%20Connected%20Scatter%20plot_static.pdf)
  * 📄 [Scatter Plot Interactive](../../reports/Relational/Scatter%20Plot_interactive.pdf)
  * 📄 [Scatter Plot Static](../../reports/Relational/Scatter%20Plot_static.pdf)
  * 📄 [Weekly Website Traffic Area Chart Interactive](../../reports/Relational/Weekly%20Website%20Traffic%20Area%20Chart_interactive.pdf)
  * 📄 [Weekly Website Traffic Area Chart Static](../../reports/Relational/Weekly%20Website%20Traffic%20Area%20Chart_static.pdf)
<!-- PDF_LIST_END -->
