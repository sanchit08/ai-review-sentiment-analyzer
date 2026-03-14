from typing import TypedDict, Annotated, Optional

class ReviewAnalysis(TypedDict):

    key_themes: Annotated[
        list[str],
        "Main product aspects discussed like sound, battery, design, price"
    ]

    summary: Annotated[
        str,
        "A short summary of the review"
    ]

    sentiment: Annotated[
        str,
        "Overall sentiment: positive, negative, neutral"
    ]

    pros: Annotated[
        Optional[list[str]],
        "List of advantages mentioned in the review"
    ]

    cons: Annotated[
        Optional[list[str]],
        "List of disadvantages mentioned in the review"
    ]