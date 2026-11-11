# CREST

**Aircraft trajectory prediction with representative–complementary hypothesis selection.**

> **Public preview.** The full implementation will be released upon acceptance of the paper.

## Overview

CREST is a framework for multi-hypothesis aircraft trajectory prediction. It combines conditioned hypothesis generation, motion-aware latent refinement, and quality estimation with representative–complementary subset selection to produce compact sets of future trajectories.

The framework consists of three components:

- **Hypothesis generation:** generate a pool of candidate future trajectories conditioned on the observed history.
- **Latent refinement:** refine the trajectory hypotheses using motion-aware latent representations.
- **Subset selection:** select representative and complementary trajectories using estimated candidate quality.

## Evaluation setting

| Item | Setting |
| --- | --- |
| Datasets | SCAT and TrajAir |
| Observation history | 40 seconds |
| Sampling interval | 5 seconds |
| Prediction horizons | 30, 60, and 120 seconds |
| Candidate pool | 20 trajectories |
| Selected subset sizes | 1, 3, and 5 trajectories |
| Distance unit | Metres |

## Repository contents

This preview contains the project overview, a standalone release-status entry point, and a dependency reference. Training and inference will be available with the full implementation.

| File | Description |
| --- | --- |
| `README.md` | Project overview and release information. |
| `crest.py` | Standalone entry point that displays the current release status. |
| `requirements-smoke.txt` | Dependency reference for the forthcoming full-release smoke tests. |
| `.gitignore` | Limits newly tracked files to the four files in this preview. |

To display the release status:

```bash
python crest.py
```

The preview entry point uses only the Python standard library. No dependency installation is needed for this command.

## Full release

The full release will include:

- Model implementation, latent refinement, and subset selection.
- Data preparation, training, inference, and evaluation scripts.
- Experiment configurations, environment specifications, and reproduction instructions.

Release updates will be posted in this repository.
