# Fyre

> A simple Django project to explore Real Estate data and publish it to the web using Vercel.

[![Fyre](assets/img/demo.jpeg)](https://fyre.vercel.app/)

## Getting Started

### Prerequisites

- Python 3.9 (Not higher)
- Pip

### Install

To install the project, start by cloning the repository:

```bash
git clone https://github.com/MorganKryze/Fyre.git
```

Then install the dependencies:

```bash
pip install -r envs/django/requirements.txt
```

That's it! You're ready to go.

### Use

To run the project, just run the following command:

```bash
python manage.py runserver
```

If you want to run the jupyter notebooks and update it, you'll also need to install the following dependencies:

Then install the dependencies:

```bash
pip install -r envs/jupyter/requirements.txt
```

And install the dataset from this [website](https://www.data.gouv.fr/fr/datasets/demandes-de-valeurs-foncieres/).

You should be ready to run the notebooks and update the data.

Finally, to host the project on Vercel, you'll need to create a new project and link it to your repository. Then it should be good to go!

## Built With

- [Django](https://www.djangoproject.com/) - The web framework used
- [Vercel](https://vercel.com/) - The hosting platform used

## Authors

- [**Morgan Kryze**](https://github.com/MorganKryze)
- [**MailiTurong**](https://github.com/MailiTruong)
- [**sheesh3218**](https://github.com/sheesh3218)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
