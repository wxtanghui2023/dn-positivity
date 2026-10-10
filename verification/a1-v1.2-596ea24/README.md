# A1 v1.2 Gate C review materials

Dedicated verification directory; files publish unchanged from the workspace repository.

- round-1 archive (frozen, immutable): `c227e3e`
- v1.2 candidate delivery node: `69d82ca`
- Gate C review baseline: `596ea24` (reviewed files), `85d161a` (self-check helper)

## Files and sha256

| `A1-v1.2-CONSISTENCY-CHECK.json` | `de1076ae77f0922377c8a78ef690fdada8cc686416e047cf1637ecc6394f2461` |
| `A1-v1.2-PREFLIGHT-CALIBRATION-PLAN.md` | `8eae6961278fb6e04b75db95b3458a4766b5871139f282a914b960c792a06cec` |
| `A1-v1.2-PREREGISTRATION-DRAFT.json` | `32e8882ff1fa022e10689e5a43700d693f9070cfc77fa02221a0b93e2ea61300` |
| `A1-v1.2-PREREGISTRATION-DRAFT.md` | `fd54014fc59afd98f651acd9cd5acac6dbd0b8ffbf0ee7834fd178fe72f4793c` |
| `A1-v1.2-R2-TEST-RESULTS.json` | `94a0ef4d91f35cb9b9a66bd0fb91fde143acbb3df3138da174faf7fadb93fd53` |
| `A1-v1.2-SPEC-CANDIDATE-r2.md` | `443bd9e2791e2cbc1a6790996ad4a4cbbba3db33fe81b1f506e1436d55a71b2c` |
| `check_v12_consistency.py` | `28aa0f050eabcd0f80dced40ad17849483fd3f77d5f3b9a5ee7d1d37b6de4363` |
| `l8_1_a12_r2_tests.py` | `320d01cc542141404e4cd9dbd4160b40034d1880506a92998a5220be13f24f4d` |

## Verify

```
sha256sum -c SHA256SUMS.txt
```

## Standing constraints

- Round 1 is frozen and must NOT be re-judged. The round-1 cross-domain submission would be
  rejected under the r2 explicit-null convention for a FORMAT reason; that is NOT capability
  evidence about r2 and must not be used as such.
- Gate C has NOT passed; the pre-registration draft is DRAFT / NOT APPROVED; no model calls
  are authorised.
- Declared open items: (4) runner integration NOT VERIFIED - the r2 scorer currently lives in
  the test module and no experiment runner imports it yet; (5) documentation gap - the
  readable pre-registration draft does not yet carry the explicit prohibition on using the
  round-1 submission as capability evidence (present in the r2 specification section 5).
