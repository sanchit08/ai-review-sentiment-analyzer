from src.extractor import extract_reviews_from_pdf
from src.analyzer import ReviewAnalyzer
from src.utils import save_json, save_csv


def main():

    print("Loading reviews from PDF...")

    reviews = extract_reviews_from_pdf("data/reviews.pdf")

    print(f"{len(reviews)} reviews found")

    analyzer = ReviewAnalyzer()

    results = []

    for i, review in enumerate(reviews):

        print(f"\nAnalyzing Review {i+1}")

        analysis = analyzer.analyze_review(review)

        analysis["review_text"] = review

        results.append(analysis)

    save_json(results, "outputs/results.json")
    save_csv(results, "outputs/results.csv")

    print("\nAnalysis completed")
    print("Results saved in outputs folder")


if __name__ == "__main__":
    main()