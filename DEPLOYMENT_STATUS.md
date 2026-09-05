# Deployment status

STATUS:
Permanent public deployment verified on Streamlit Community Cloud.

PERMANENT APP:
https://u87mg-cell-analysis-public-viuiux8fjkwnnncax2eupz.streamlit.app/?embed=true

PROFESSOR-FACING ALIAS:
https://jiaweiliu555.github.io/u87mg-cell-analysis-link/

ALIAS STATUS:
The GitHub Pages alias now redirects to the permanent Streamlit app's public embed route. The former Quick Tunnel is no longer used.

HOSTING:
Streamlit Community Cloud. The app is hosted independently of the Mac and uses the sanitized public deployment mirror:
https://github.com/JiaweiLiu555/u87mg-cell-analysis-public

PRIVATE SOURCE REPOSITORY:
https://github.com/JiaweiLiu555/u87mg-cell-analysis

RELEASE ENTRYPOINT:
deploy_app.py

DEPLOYMENT BUNDLE:
Dockerfile, requirements.deploy.txt, .streamlit/config.toml, deploy_app.py, conservative input QC code, and approved historical demonstration overlays. Raw thesis files, raw lab images, virtual environments, caches, and secrets are excluded from the public deployment mirror.

EXTERNAL VERIFICATION:
The permanent embed URL returned HTTP 200, Streamlit initialized the app, both demonstration choices were available, and the Crystal Violet demonstration rendered the annotated view with an automated candidate count of 110 and a manual-verification status.

SCIENTIFIC STATUS:
Fixed/crystal-violet and neurosphere outputs are candidate measurements from historical demonstration figures and require manual review. Live phase contrast is experimental. No biological accuracy, viability, calibrated probability, or authoritative category claim is made.

MAC REQUIREMENT:
No. The public app does not depend on a local process or Quick Tunnel.

TEST STATUS:
The permanent app booted and was exercised through the public embed route. Local validated tests include the prior 15-test suite and 3 imaging checks; release-safety and conservative input-QC tests remain tracked in the repository. Biological validation remains pending independent Dr. Smith data.

NEXT REQUIRED ACTION:
Dr. Smith must provide independent raw U87MG microscopy images and trusted reference measurements before biological performance can be estimated.
