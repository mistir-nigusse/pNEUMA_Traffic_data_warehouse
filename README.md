# Traffic Data Warehouse Project

This project is aimed at creating a scalable data warehouse to manage vehicle trajectory data collected by swarm UAVs and static roadside cameras. The data will be used by the city's traffic department to improve traffic flow and support other undisclosed projects.

## Folder Structure
```bash
TRAFFIC_DATA_WEEK_2
│
├── config
│ 
│
├── dags
│ ├── development
│ ├── production
│ │ └── csv_to_postgres_dag.py
│ └── staging
│
├── data
│
├── utils
│ └── utils.py
│
├── logs
│
├── plugins
│
├── .env
│
├── .gitignore
│
├── docker-compose.yaml
│
├── LICENSE
│
└── Screenshots
```
## Description

- **config:** Contains configuration files.
  - **config.py:** Configuration settings for the project.

- **dags:** Contains Directed Acyclic Graphs (DAGs) for Airflow.
  - **development:** Development environment DAGs.
  - **production:** Production environment DAGs.
    - **csv_to_postgres_dag.py:** DAG for moving CSV data to PostgreSQL.
  - **staging:** Staging environment DAGs.

- **data:** Data storage directory.

- **utils:** Utility functions for the project.
  - **utils.py:** Common utility functions.

- **logs:** Directory for storing logs.

- **plugins:** Airflow plugins.

- **.env:** Environment variables file.

- **.gitignore:** Gitignore file to exclude certain files from version control.

- **docker-compose.yaml:** Docker Compose file for setting up the project environment.

- **LICENSE:** License information for the project.

- **Screenshots:** Directory for storing project screenshots.

## Usage

1. Clone the repository.
2. Set up your environment variables in `.env`.
3. Run `docker-compose up` to start the project.

## License

This project is licensed under the [MIT License](LICENSE).
