from __future__ import annotations

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskRetrieval import AbsTaskRetrieval


class LegalSummarization(AbsTaskRetrieval):
    metadata = TaskMetadata(
        name="LegalSummarization",
        description="The dataset consistes of 439 pairs of contracts and their summarizations from https://tldrlegal.com and https://tosdr.org/.",
        reference="https://github.com/lauramanor/legal_summarization",
        dataset={
            "path": "mteb/legal_summarization",
            "revision": "3bb1a05c66872889662af04c5691c14489cebd72",
        },
        type="Retrieval",
        category="s2p",
        modalities=["text"],
        eval_splits=["test"],
        eval_langs=["eng-Latn"],
        main_score="ndcg_at_10",
        date=None,
        domains=["Legal", "Written"],
        task_subtypes=["Article retrieval"],
        license="apache-2.0",
        annotations_creators="derived",
        dialect=None,
        sample_creation="found",
        bibtex_citation=r"""
@inproceedings{manor-li-2019-plain,
  address = {Minneapolis, Minnesota},
  author = {Manor, Laura  and
Li, Junyi Jessy},
  booktitle = {Proceedings of the Natural Legal Language Processing Workshop 2019},
  month = jun,
  pages = {1--11},
  publisher = {Association for Computational Linguistics},
  title = {Plain {E}nglish Summarization of Contracts},
  url = {https://www.aclweb.org/anthology/W19-2201},
  year = {2019},
}
""",
    )
