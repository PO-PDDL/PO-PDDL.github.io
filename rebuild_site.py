#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import subprocess
from pathlib import Path
from textwrap import dedent


CSS_TEMPLATE = dedent(
    """
    :root {
      --text-primary: #222;
      --text-secondary: #555;
      --text-muted: #777;
      --border-color: #d9d9d9;
      --light-bg: #f5f5f5;
      --section-bg: #fafafa;
      --link-color: #3273dc;
    }

    html {
      scroll-behavior: smooth;
    }

    body {
      font-family: 'Inter', 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif;
      color: var(--text-primary);
      line-height: 1.6;
      background: #fff;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }

    img,
    video {
      display: block;
      max-width: 100%;
    }

    .project-hero {
      background: #fff;
    }

    .hero-body {
      padding: 3rem 1.5rem 2rem;
    }

    .hero-copy {
      max-width: 1120px;
      margin: 0 auto;
    }

    .eyebrow,
    .section-kicker {
      display: none;
    }

    .project-title,
    .publication-title {
      font-weight: 700 !important;
      line-height: 1.15 !important;
      color: var(--text-primary) !important;
      margin-bottom: 1rem !important;
    }

    .project-title {
      font-size: clamp(1.9rem, 3vw, 2.9rem);
    }

    .project-subtitle {
      color: var(--text-secondary);
      font-size: 1.05rem;
      max-width: 760px;
      margin: 0 auto;
    }

    .hero-actions {
      margin-top: 1.5rem;
      display: flex;
      flex-wrap: wrap;
      gap: 0.75rem;
      justify-content: center;
    }

    .button {
      border-radius: 10px !important;
      font-weight: 600 !important;
      box-shadow: none !important;
      transition: none !important;
    }

    .button.is-dark {
      background: #363636 !important;
    }

    .hero-secondary {
      background: #fff !important;
      border: 1px solid var(--border-color) !important;
      color: var(--text-primary) !important;
    }

    .section-tight {
      padding: 2rem 1.5rem 0;
    }

    .abstract-section,
    .results-section {
      background: var(--section-bg);
    }

    .abstract-section .container,
    .project-footer .container {
      max-width: 1120px;
    }

    .section-heading {
      margin-bottom: 1.25rem;
    }

    .section-heading .title {
      margin-bottom: 0.5rem !important;
    }

    .section-description {
      color: var(--text-secondary);
      max-width: 760px;
      margin: 0 auto;
    }

    .abstract-copy {
      color: var(--text-primary);
      font-size: 1rem;
    }

    .figure-panel {
      margin: 0 auto;
    }

    .figure-panel img {
      width: 100%;
      border: 1px solid var(--border-color);
    }

    .pipeline-section {
      padding-top: 1rem;
    }

    .pipeline-image {
      width: 100%;
    }

    .demo-section {
      background: #fff;
    }

    .demo-grid {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 1.5rem;
      align-items: start;
    }

    .demo-card {
      border: 1px solid var(--border-color);
      padding: 0.9rem;
      background: #fff;
      border-radius: 8px;
    }

    .demo-card-wide {
      grid-column: auto;
    }

    .demo-video {
      width: 100%;
      aspect-ratio: 2 / 3;
      object-fit: cover;
      background: #000;
      border: 1px solid var(--border-color);
      border-radius: 6px;
    }

    .demo-instruction {
      margin-top: 0.8rem;
      color: var(--text-secondary);
      font-size: 0.97rem;
    }

    .demo-instruction-top {
      margin-top: 0;
      margin-bottom: 0.75rem;
      color: var(--text-primary);
      font-size: 0.97rem;
      min-height: 4.8em;
    }

    .results-section {
      padding-bottom: 2.75rem;
    }

    .project-footer {
      background: #fff;
      padding: 2rem 1.5rem 2.5rem;
      border-top: 1px solid var(--border-color);
    }

    .project-footer a,
    a {
      color: var(--link-color);
    }

    @media screen and (max-width: 900px) {
      .demo-grid {
        grid-template-columns: 1fr;
      }

      .demo-instruction-top {
        min-height: 0;
      }
    }

    @media screen and (max-width: 768px) {
      .hero-body {
        padding: 2.25rem 1rem 1.5rem;
      }

      .section-tight {
        padding: 2rem 1rem 0;
      }
    }

    .is-disabled {
      opacity: 0.7;
      cursor: default;
      pointer-events: none;
    }
    """
).strip() + "\n"


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="title" content="{title}">
  <meta name="description" content="{meta_description}">
  <meta name="keywords" content="POMDP, PDDL, robot planning, partial observability, symbolic planning, visual demonstrations">
  <meta name="author" content="PO-PDDL">
  <meta name="theme-color" content="#2563eb">
  <title>PO-PDDL | Learning Symbolic POMDPs from Visual Demonstrations</title>
  <link rel="icon" type="image/x-icon" href="static/images/favicon.ico">
  <link rel="stylesheet" href="static/css/bulma.min.css">
  <link rel="stylesheet" href="static/css/index.css">
  <link rel="preload" href="static/css/fontawesome.all.min.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
  <link rel="preload" href="https://cdn.jsdelivr.net/gh/jpswalsh/academicons@1/css/academicons.min.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
  <noscript>
    <link rel="stylesheet" href="static/css/fontawesome.all.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/jpswalsh/academicons@1/css/academicons.min.css">
  </noscript>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <script defer src="static/js/fontawesome.all.min.js"></script>
</head>
<body>
  <main>
    <section class="hero project-hero">
      <div class="hero-body">
        <div class="container is-max-widescreen">
          <div class="hero-copy has-text-centered">
            <p class="eyebrow">Project Page</p>
            <h1 class="title project-title">{title}</h1>
            <div class="hero-actions">
              <a class="button is-dark is-disabled" href="javascript:void(0)" aria-disabled="true">
                <span class="icon"><i class="ai ai-arxiv"></i></span>
                <span>arXiv (Coming Soon)</span>
              </a>
              <a class="button is-dark is-disabled" href="javascript:void(0)" aria-disabled="true">
                <span class="icon"><i class="fab fa-github"></i></span>
                <span>Code (Coming Soon)</span>
              </a>
              <a class="button is-dark" href="#demo-videos">
                <span class="icon"><i class="fas fa-play-circle"></i></span>
                <span>View Demos</span>
              </a>
              <a class="button is-dark" href="#experimental-results">
                <span class="icon"><i class="fas fa-chart-line"></i></span>
                <span>Results</span>
              </a>
              <a class="button is-dark" href="prompt-library/index.html">
                <span class="icon"><i class="fas fa-folder-open"></i></span>
                <span>Prompt Library</span>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section section-tight pipeline-section">
      <div class="container is-max-widescreen">
        <img class="pipeline-image" src="contexts/pipeline.png" alt="PO-PDDL learning pipeline" loading="lazy">
      </div>
    </section>

    <section class="section section-tight abstract-section">
      <div class="container is-max-widescreen">
        <div class="section-heading has-text-centered">
          <h2 class="title is-3">Abstract</h2>
        </div>
        <div class="content abstract-copy">
          <p>{abstract}</p>
        </div>
      </div>
    </section>

    <section class="section section-tight demo-section" id="demo-videos">
      <div class="container is-max-widescreen">
        <div class="section-heading has-text-centered">
          <h2 class="title is-3">Demo Videos</h2>
        </div>
        <div class="demo-grid">
{demo_cards}
        </div>
      </div>
    </section>

    <section class="section section-tight results-section" id="experimental-results">
      <div class="container is-max-widescreen">
        <div class="section-heading has-text-centered">
          <h2 class="title is-3">Experimental Results</h2>
        </div>
        <figure class="figure-panel results-panel">
          <img src="contexts/experimental%20results/comparison_results.png" alt="Experimental comparison results" loading="lazy">
        </figure>
      </div>
    </section>
  </main>

  <footer class="footer project-footer">
    <div class="container">
      <div class="content has-text-centered">
        <p>This page was adapted from the <a href="https://github.com/eliahuhorwitz/Academic-project-page-template" target="_blank">Academic Project Page Template</a>.</p>
      </div>
    </div>
  </footer>
</body>
</html>
"""


def shell_quote(path: Path) -> str:
    text = str(path)
    return "'" + text.replace("'", "'\"'\"'") + "'"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()


def compress_whitespace(text: str) -> str:
    return " ".join(text.split())


def build_demo_card(video_rel: str, instruction: str) -> str:
    safe_instruction = html.escape(instruction)
    safe_video = html.escape(video_rel)
    return (
        "          <article class=\"demo-card\">\n"
        f"            <p class=\"demo-instruction demo-instruction-top\">{safe_instruction}</p>\n"
        "            <video class=\"demo-video\" controls preload=\"metadata\">\n"
        f"              <source src=\"{safe_video}\" type=\"video/mp4\">\n"
        "            </video>\n"
        "          </article>"
    )


def ensure_demo_video(task_dir: Path, *, ffmpeg_bin: str, overwrite: bool) -> str:
    high = task_dir / "cam_high.mp4"
    wrist = task_dir / "cam_right_wrist.mp4"
    output = task_dir / "combined_vertical_2x_browser.mp4"
    if not high.exists() or not wrist.exists():
        raise FileNotFoundError(f"Missing source videos under {task_dir}")

    sources = [high, wrist]
    if output.exists() and not overwrite:
        output_mtime = output.stat().st_mtime
        newest_source_mtime = max(path.stat().st_mtime for path in sources)
        if output_mtime >= newest_source_mtime:
            return output.name

    filter_complex = (
        "[0:v]scale=640:480[top];"
        "[1:v]scale=640:480[bottom];"
        "[top][bottom]vstack=inputs=2[stack];"
        "[stack]setpts=0.5*PTS,"
        "drawtext=text='2x':x=22:y=22:fontcolor=white:fontsize=34:"
        "box=1:boxcolor=0x111827AA:boxborderw=10[v]"
    )

    cmd = (
        f"{ffmpeg_bin} -y "
        f"-i {shell_quote(high)} "
        f"-i {shell_quote(wrist)} "
        f"-filter_complex {shell_quote(filter_complex)} "
        f"-map '[v]' -an "
        "-c:v libx264 -profile:v high -level 4.0 "
        "-pix_fmt yuv420p -movflags +faststart "
        "-r 10 -g 20 -preset medium -crf 20 "
        f"{shell_quote(output)}"
    )
    subprocess.run(cmd, shell=True, check=True)
    return output.name


def render_index(root: Path, *, title: str, abstract: str, demo_cards: list[str]) -> None:
    meta_description = compress_whitespace(abstract)
    if len(meta_description) > 158:
        meta_description = meta_description[:155].rstrip() + "..."
    html_text = HTML_TEMPLATE.format(
        title=html.escape(title),
        abstract=html.escape(abstract),
        meta_description=html.escape(meta_description),
        demo_cards="\n".join(demo_cards),
    )
    (root / "index.html").write_text(html_text, encoding="utf-8")


def write_css(root: Path) -> None:
    (root / "static" / "css" / "index.css").write_text(CSS_TEMPLATE, encoding="utf-8")


def collect_task_dirs(demo_root: Path) -> list[Path]:
    return sorted(
        (path for path in demo_root.iterdir() if path.is_dir() and path.name.startswith("task_")),
        key=lambda p: p.name,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Rebuild the PO-PDDL website from contexts/ assets.")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parent,
        help="Website root directory. Defaults to this script's directory.",
    )
    parser.add_argument(
        "--skip-videos",
        action="store_true",
        help="Skip ffmpeg video rebuilding and only regenerate HTML/CSS.",
    )
    parser.add_argument(
        "--ffmpeg-bin",
        default="ffmpeg",
        help="Path to ffmpeg binary.",
    )
    parser.add_argument(
        "--overwrite-videos",
        action="store_true",
        help="Force rebuild of combined demo videos even if outputs already exist.",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    contexts = root / "contexts"
    demo_root = contexts / "demo_videos"

    title = read_text(contexts / "title.txt")
    abstract = compress_whitespace(read_text(contexts / "abstract.txt"))

    demo_cards: list[str] = []
    for task_dir in collect_task_dirs(demo_root):
        instruction = compress_whitespace(read_text(task_dir / "instruction.txt"))
        video_name = "combined_vertical_2x_browser.mp4"
        if not args.skip_videos:
            video_name = ensure_demo_video(
                task_dir,
                ffmpeg_bin=args.ffmpeg_bin,
                overwrite=args.overwrite_videos,
            )
        elif not (task_dir / video_name).exists():
            raise FileNotFoundError(
                f"{task_dir / video_name} is missing. Re-run without --skip-videos."
            )
        rel_video = f"contexts/demo_videos/{task_dir.name}/{video_name}"
        demo_cards.append(build_demo_card(rel_video, instruction))

    render_index(root, title=title, abstract=abstract, demo_cards=demo_cards)
    write_css(root)

    print(f"Rebuilt website under {root}")
    print(f"Generated {len(demo_cards)} demo entries.")
    if args.skip_videos:
        print("Skipped video rebuild.")
    else:
        print("Rebuilt combined 2x browser-compatible videos.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
