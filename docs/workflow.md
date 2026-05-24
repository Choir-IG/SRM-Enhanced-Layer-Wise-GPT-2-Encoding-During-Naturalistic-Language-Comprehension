# Analysis workflow

1. `notebooks/01_srm_fixed_srm50_pipeline.ipynb`
   - Builds Schaefer network ROIs.
   - Fits fixed-dimension SRM models with 50 features and 10 iterations.
   - Evaluates between-subject time-segment classification.

2. `notebooks/02_layerwise_gpt2_encoding_pipeline.ipynb`
   - Extracts GPT-2 XL layer-wise representations.
   - Builds TR-level delayed design matrices.
   - Fits Raw+LLM and SRM+LLM encoding models.
   - Generates layer-wise encoding summaries and brain maps.

3. `notebooks/03_exploratory_parcel_layer_network_analysis.ipynb`
   - Exploratory parcel-level decomposition of network-level effects.
   - Used to inspect parcel hotspots, preferred layer depth, heterogeneity,
     and spatial gradients.

4. `notebooks/04_exploratory_functional_lateralization_analysis.ipynb`
   - Exploratory hemisphere and lateralization-index analyses.
   - Includes denominator-threshold validation for lateralization indices.

5. `R/05_final_layerwise_hemisphere_statistics.Rmd`
   - Main organized R statistics for layer-wise hemisphere effects.
   - Reports mixed-effects models, Welch tests, permutation checks, and final
     FDR-significant result tables.

6. `R/06_exploratory_parcel_summary_statistics.Rmd`
   - Additional exploratory parcel-summary statistics.
