from __future__ import annotations

from mteb.abstasks.AbsTaskBitextMining import AbsTaskBitextMining
from mteb.abstasks.MultilingualTask import MultilingualTask
from mteb.abstasks.TaskMetadata import TaskMetadata

_LANGUAGES = {
    "en-ha": ["eng-Latn", "hau-Latn"],
    "en-ig": ["eng-Latn", "ibo-Latn"],
    "en-pcm": ["eng-Latn", "pcm-Latn"],
    "en-yo": ["eng-Latn", "yor-Latn"],
}


class NollySentiBitextMining(AbsTaskBitextMining, MultilingualTask):
    metadata = TaskMetadata(
        name="NollySentiBitextMining",
        dataset={
            "path": "gentaiscool/bitext_nollysenti_miners",
            "revision": "d48254fbdb51af1ae7f20831aab0bccf0b70a19c",
        },
        description="NollySenti is Nollywood movie reviews for five languages widely spoken in Nigeria (English, Hausa, Igbo, Nigerian-Pidgin, and Yoruba.",
        reference="https://github.com/IyanuSh/NollySenti",
        type="BitextMining",
        category="s2s",
        modalities=["text"],
        eval_splits=["train"],
        eval_langs=_LANGUAGES,
        main_score="f1",
        date=("2022-01-01", "2023-01-01"),
        domains=["Social", "Reviews", "Written"],
        task_subtypes=[],
        license="cc-by-sa-4.0",
        annotations_creators="human-annotated",
        dialect=[],
        sample_creation="found",
        bibtex_citation=r"""
@inproceedings{shode2023nollysenti,
  author = {Shode, Iyanuoluwa and Adelani, David Ifeoluwa and Peng, Jing and Feldman, Anna},
  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},
  pages = {986--998},
  title = {NollySenti: Leveraging Transfer Learning and Machine Translation for Nigerian Movie Sentiment Classification},
  year = {2023},
}
""",
    )
