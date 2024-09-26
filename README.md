# Sign Language Recognition Model

This repository contains the code for training a Sign Language Recognition (SLR) model based on skeleton images.

This is a simpler version of the original code, which was designed for experiments. We are working to make it more user-friendly.

If you would like to know more about the original code, please check the [original repository](https://github.com/Dudu197/sign-language-recognition).

# How to use

## Requirements

Install the requirements using the following command:

```bash
pip install -r requirements.txt
```

## Dataset

The code was tested using the MINDS-Libras dataset. It can be downloaded [here](https://drive.google.com/file/d/1qx2JudpjPgpp4-fpJ7YVMrszWV4lYPCd/view?usp=drive_link).

The code expects the dataset to be in `datasets` folder.

## Training

To train the model, you can use the following command:

```bash
sh train.sh
```

The script will train the model using the MINDS-Libras dataset and save the results in the `results` folder.
