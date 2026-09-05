# Release gate

This gate separates reproducible software behavior from biological evidence. PASS means the current software check is complete; PENDING means independent U87MG biological validation is still required.

| Mode | Software | Sanity tests | Visual audit | Biological validation | Professor-facing status |
|---|---|---|---|---|---|
| Fixed / crystal violet | PASS | PASS | PASS | PENDING | EXPERIMENTAL |
| Neurosphere / aggregate | PASS | PASS | PASS | PENDING | EXPERIMENTAL |
| Live phase contrast | PASS | PASS | PASS | PENDING | EXPERIMENTAL |

## Gate interpretation

- Fixed mode reports attached stained-cell candidate regions, never direct live/dead counts.
- Neurosphere mode reports aggregate candidates and pixel-based morphology; exact cell counts inside dense aggregates are not enabled.
- Live mode is limited to experimental morphology proposals and does not expose viability, dead-count, or calibrated-probability claims.
- Demos are historical thesis figures for software demonstration only.
- The required independent validation domain is Dr. Smith's raw U87MG microscopy data and trusted reference measurements.

