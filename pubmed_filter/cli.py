import argparse
from pubmed_filter.fetch_papers import fetch_papers, get_paper_details
from pubmed_filter.filter_papers import filter_papers
from pubmed_filter.save_results import save_to_csv

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with non-academic authors.")
    parser.add_argument("query", help="Search query for PubMed")
    parser.add_argument("-f", "--file", help="Filename to save results", default="output.csv")
    parser.add_argument("-n", "--num", type=int, help="Number of papers to fetch", default=10)
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")

    args = parser.parse_args()

    print(f"Fetching {args.num} papers for query: {args.query}")

    paper_ids = fetch_papers(args.query, args.num)

    if args.debug:
        print(f"🔹 Retrieved Paper IDs: {paper_ids}")

    papers = [get_paper_details(pid) for pid in paper_ids]

    if args.debug:
        print(f"🔹 Raw Paper Details: {papers}")

    filtered_papers = filter_papers(papers)

    if args.debug:
        print(f"🔹 Filtered Papers: {filtered_papers}")

    if filtered_papers:
        save_to_csv(filtered_papers, args.file)
        print(f"Results saved to {args.file}")
    else:
        print("No non-academic papers found.")

if __name__ == "__main__":
    main()
