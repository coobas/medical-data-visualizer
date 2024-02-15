# Medical Data Visualizer

This project is adopted from the [freeCodeCamp](https://www.freecodecamp.org/)
[Data Analysis with Python course](https://www.freecodecamp.org/learn/data-analysis-with-python/).

To start working on the project, you need to [**fork** this repository](https://github.com/coobas/medical-data-visualizer/fork) to your own GitHub account. Then, clone the new repository to your computer
and start working on the project.

## Conda virtual environment

```
conda create -n med-vis -c conda-forge python=3.11
conda activate med-vis
```

Install necessary libriries
```
conda install streamlit pandas plotly
```


## Part 1: Data processing and visualization

Follow the freeCodeCamp instructions for building your project at https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/medical-data-visualizer


## Part 2: Web application

In the second part, we will build a simple application using the [Streamlit]](https://streamlit.io/) library.

Quoting the Streamlit web site:
> A faster way to build and share data apps
>
> Streamlit turns data scripts into shareable web apps in minutes.
All in pure Python. No front‑end experience required.

* Streamlit is really efficient in creating web applications, mainly for data science projects.
* The result is visually appealing.
* It is easy to deploy.

### 1. Install Streamlit

If not already installed, install Streamlit using [the official instructions](https://docs.streamlit.io/en/stable/installation.html).

### 2. Turn your code into a Streamlit app

1. Turn `medical_data_visualizer.py` into a reusable module.
    1. Wrap the code that creates the `df` dataframe into a function called `load_data()`. This function should return the dataframe.
    2. Change the plotting functions to accept a dataframe as an argument.
    3. (Optional) Adapt the test to work with the new module.

2. Using instructions at https://docs.streamlit.io/library/get-started/create-an-app,
create your first Streamlit app 🎉 in a new `app.py` file:
    1. Import the `medical_data_visualizer` module.
    2. Add a title to your app.
    2. Load the dataframe using the `load_data()` function.
    3. Display the two figures using either the `st.pyplot` or `st.write` function. Optionally, you can add a header above each figure.

3. Add some user controls (first, we need to make the functions in `medical_data_visualizer` accept arguments for the user controls):
    1. Change functions to accept these arguments:
        - `load_data(bmi_overweight=25)`
        - `draw_cat_plot(df, split_by="cardio")`
        - `draw_heat_map(df, outlier_quantile=0.025)`
    2. Add a sidebar to your app containing:
        - a slider for the `bmi_overweight` argument
        - a selectbox for the `split_by` argument
        - a number input for the `outlier_quantile` argument

4. Publish the app using instructions at https://docs.streamlit.io/en/stable/deploy_streamlit_app.html.

You will need to:
    1. Create a `requirements.txt` file containing the list of dependencies. See [pip documentation](https://pip.pypa.io/en/stable/reference/requirements-file-format/) for instructions. Remember you need to add all the primary dependencies, such as `pandas` or `seaborn`, and also `streamlit`. It is advisable to specify the versions of the dependencies, e.g. to pin the major versions using `~=`.
    2. Commit all changes and push to your GitHub repository.
    3. Publish the app and share the link 😏

5. Change the plotting library to [Plotly Express](https://plotly.com/python/plotly-express/) and re-implement the plotting functions to use Plotly Express.
