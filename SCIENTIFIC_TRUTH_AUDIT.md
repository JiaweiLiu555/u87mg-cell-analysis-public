# Scientific truth audit

## Release conclusion

This repository currently supports reproducible software demonstrations and conservative image/QC review. It does not yet establish biological performance on Dr. Smith's independent raw U87MG microscopy images with trusted reference measurements. The public release therefore uses candidate language, descriptive review states, visible overlays for demonstrations, and no calibrated confidence or viability claims.

Historical thesis figures are used only for software demonstration and visual inspection. They are not training data, independent validation data, or a source of invented ground truth.

## Visible output audit

| Output shown | Meaning and calculation | Software evidence | Biological status | Release treatment |
|---|---|---|---|---|
| Automated candidate count | Number of regions returned by the selected demonstration pipeline. Fixed mode counts segmented attached stained regions; aggregate mode counts segmented aggregate regions. | Deterministic demo generation, object tables, QC outputs, and imaging tests. | Not validated against independent U87MG human counts. | Labeled 'Automated candidate count' or 'Aggregate candidates'; manual verification recommended. |
| Image QC | Descriptive input/status state from deterministic file and image checks. It is not a probability or accuracy score. | Input safety tests cover blank, extreme, tiny, oversized, and structured inputs. | A QC pass does not establish biological correctness. | Use 'Reviewable input' or 'Manual review required'; no numeric QC score. |
| Image dimensions and mean grayscale | File-level pixel dimensions and grayscale summary computed from the uploaded image. | Pillow computation and export tests. | Descriptive only; not a cell measurement. | Enabled for upload review; no biological interpretation. |
| Aggregate area | Pixel area of a segmented aggregate region. | Imaging module tests and generated object CSVs. | Not independently validated on Dr. Smith's data. | Available in inspectable local/generated outputs; report pixels only without calibration. |
| Equivalent diameter | Diameter derived from measured pixel area, in pixels. | Imaging module tests and generated object CSVs. | Morphometric proxy, not an exact cell count or biological category. | Pixels only unless explicit calibration exists. |
| Coverage | Fraction of image pixels assigned to segmented aggregate regions. | Imaging module tests and generated QC outputs. | Not a validated neurosphere assay endpoint for this lab yet. | Do not show as a placeholder on public demo; expose only when computed from the analyzed image and mark for review. |
| Provisional morphology category | Rule-based size/shape grouping. | Deterministic category code is covered by imaging tests. | Numeric boundaries are not Dr. Smith-approved biological thresholds. | If present, label 'Provisional morphology category' and keep thresholds transparent/configurable. |
| Live morphology candidates | Heuristic morphology proposals based on visible shape/attachment features. | Non-biological smoke tests and deterministic imaging checks. | Morphology alone has not demonstrated live/dead reliability on independent U87MG images; detached cells may be absent. | Publicly marked 'Experimental'; never show live count, dead count, viability percentage, or calibrated probability. |
| Confidence, probability, certainty, accuracy | None of these is a calibrated quantity in the current release. | No appropriate held-out calibration dataset exists. | Unsupported. | Removed from public results; descriptive review states are used instead. |
| Automatic image-mode prediction | No automatic mode claim is made; the user explicitly selects a workflow. | UI workflow test. | Avoids unsupported mode inference. | Enabled only as explicit user selection. |

## Mode truth gates

### Fixed and crystal violet

The endpoint is attached stained-cell quantification, not direct live/dead analysis. Purple-stain extraction and region segmentation are useful software operations, but stain, debris, touching objects, clusters, illumination, and edge artifacts can all require human review. Demonstration counts are candidate counts only.

### Neurosphere and aggregate

Aggregate regions, pixel area, equivalent pixel diameter, and coverage can be computed when segmentation is valid. Dense aggregate images do not justify exact individual-cell counts. Starting, small, medium, large, and well-covered labels are provisional morphology categories unless Dr. Smith approves thresholds.

### Live phase contrast

This mode is experimental. Rounded and spindle-like morphology candidates are not equivalent to dead and viable cells. The release does not present biological viability metrics or calibrated probabilities.

## Safety and provenance

- Unsupported or corrupted uploads are rejected or warned; an internal failure must not become a confident zero.
- No physical unit is shown unless pixel calibration is explicitly supplied.
- Original uploads are handled transiently by the application code and are not intentionally written to the repository or sent to a third-party AI API.
- Every thesis demonstration is visibly marked as historical and non-validation data.
- Candidate results should be paired with the annotated overlay and exported table so a researcher can inspect what was counted.

## What remains blocked

Biological validation requires independent raw U87MG images, field/well/experiment provenance, trusted human or assay reference measurements, and predeclared evaluation rules from Dr. Smith. Until then, software validation must not be presented as biological validation.

