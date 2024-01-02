# Developemnt

# - name: Upload coverage report to Codecov
      #   uses: codecov/codecov-action@v2
      #   with:
      #     token: ${{ secrets.CODECOV_TOKEN }}
      #     fail_ci_if_error: true


      - name: Release
        uses: softprops/action-gh-release@v1
        with:
          body_path: "./docs/CHANGELOG.md"
          tag_name: ${{ env.REVISION }}
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

      - name: Create PyPI release
        run: |
          poetry config pypi-token.pypi ${{ secrets.PYPI_TOKEN }}
          poetry publish --build