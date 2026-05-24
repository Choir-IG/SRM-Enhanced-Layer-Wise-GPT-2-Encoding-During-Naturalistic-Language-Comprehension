# SRM-Enhanced-Layer-Wise-GPT-2-Encoding-During-Naturalistic-Language-Comprehension
This repository contains the code used for an SNL 2026 analysis of shared response modeling (SRM), GPT-2 XL layer-wise encoding, parcel-level cortical mapping, and exploratory hemispheric lateralization during naturalistic story comprehension.

The repository is code-only. Raw fMRI data, atlas files, transcripts, audio,
and generated outputs are not included.

## Data And Method References

The original fMRI data can be found in the OpenNeuro Narratives dataset
([ds002345 version 1.1.4](https://openneuro.org/datasets/ds002345/versions/1.1.4)),
described in *The "Narratives" fMRI dataset for evaluating models of naturalistic
language comprehension*. The SRM analysis logic was adapted from the
[BrainIAK SRM tutorial](https://brainiak.org/). The LLM encoding workflow was
primarily based on the deep fMRI dataset paper
([Nature Scientific Data](https://www.nature.com/articles/s41597-023-02437-z))
and the associated GitHub repository
([HuthLab/deep-fMRI-dataset](https://github.com/HuthLab/deep-fMRI-dataset)).

## Repository structure

```text
notebooks/
  01_srm_fixed_srm50_pipeline.ipynb
  02_layerwise_gpt2_encoding_pipeline.ipynb
  03_exploratory_parcel_layer_network_analysis.ipynb
  04_exploratory_functional_lateralization_analysis.ipynb
R/
  05_final_layerwise_hemisphere_statistics.Rmd
  06_exploratory_parcel_summary_statistics.Rmd
src/
  snl_paths.py
  snl_plotting.py
config/
  paths_template.yaml
data/
  README.md
docs/
  workflow.md
```

## Workflow

Run the code in this order:

1. Fixed-dimension SRM fitting and time-segment classification.
2. GPT-2 XL layer-wise Raw+LLM and SRM+LLM encoding.
3. Exploratory parcel-level decomposition.
4. Exploratory functional lateralization.
5. Final R statistics for layer-wise hemisphere effects.
6. Optional exploratory parcel-summary R statistics.

## Path setup

All private local paths were removed. Before running the notebooks, replace
the `YOUR_*` placeholders with local paths, or copy `config/paths_template.yaml`
to `config/paths.yaml` and use it as a reference.

Common placeholders:

- `YOUR_PROJECT_ROOT`
- `YOUR_SNL2026_ROOT`
- `YOUR_FMRI_DATA_DIR`
- `YOUR_SCHAEFER400_ATLAS_NIFTI_PATH`
- `YOUR_SCHAEFER400_LABEL_TXT_PATH`
- `YOUR_TRANSCRIPT_TXT_PATH`
- `YOUR_WORD_ONSET_OFFSET_CSV_PATH`
- `YOUR_AUDIO_FILE_PATH`

## Python dependencies

Install the Python packages listed in `requirements.txt`.

## R dependencies

The R Markdown files use:

- `tidyverse`
- `readr`
- `ggplot2`
- `writexl`
- `broom`
- `lme4`
- `lmerTest`
- `broom.mixed`
