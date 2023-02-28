# xnt :croissant:
XNT is the most simple webapp to get a fast daily overview on arxiv research papers, in your field of interest.

Right now, you get `cs.AI` categorized papers for the past `24h`. You can change it easily in the code.

## High level architecture
### Database
[OpenSearch](https://opensearch.org/) (open source fork of ElasticSearch)

### Cron Jobs
- `jobs/import_new_papers_job.py` imports new papers into the DB.
- `jobs/gpt3_sumup_job.py` summarizes papers abstract (inc soon).

### UI
- only using [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) templating language (for the moment)


## Roadmap
1. using gpt-3 model to further reduce the paper abstract without loosing key points (very soon)
2. using gpt-3 model to sum up the entire paper
3. improve readibility 
4. provide some customization options (different categories, etc...)
5. all of this might just end up turned into a cli tool
