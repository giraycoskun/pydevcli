# Developement

## CI/CD Pipeline

``` mermaid
---
title: Developmet Flow
---
gitGraph
      commit id:"initial"
      branch stage
      branch test
      branch dev
      commit id: "feature"
      commit id: "fix"
      commit id: "chore"
      commit id: "test"
      commit id: "docs"
      checkout test
      merge dev
      checkout stage
      merge test
      commit id: "stage release"
      checkout main
      merge stage
      commit id: "publish release"

```

``` mermaid
flowchart LR
    A[Develop] -.-> B[Run Unit Tests] -.-> A[Develop]
    A[Develop] -->|Publish| C[Test]
    C[Test] -.-> D[Run Integration/Regression Tests] -.-> C[Test]
    C[Test] -->|Publish| E[Stage]
    E[Stage] -->|Prepare New Release| F[Main]
    F[Main] --> G[Publish to PyPI]
    F[Main] --> H[Upload Github Release]
```

## Notes

```yml
- name: Upload coverage report to Codecov
  uses: codecov/codecov-action@v2
  with:
    token: ${{ secrets.CODECOV_TOKEN }}
    fail_ci_if_error: true
```