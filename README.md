# Pandas tutorial 

0. Configuration

    This guide provides instructions to resolve issues with Korean fonts not displaying correctly in Matplotlib when using Jupyter Notebook in a Python environment. The solution involves installing necessary fonts, setting them up for Matplotlib, and clearing the font cache.

    0. Prerequisites

        **Matplotlib**
    
    1. Install Korean Fonts (Nanum)

        ```
        # First, install the required Korean fonts for your system.
        sudo apt update
        sudo apt-get install fonts-nanum*
        ```

    2. Rebuild Font Cache

        ```
        fc-cache -fv
        ```

    3. Verify Matplotlib's Installation Path
        
        To verify the location of your Matplotlib installation (which will help later when setting up fonts), run:
        ```
        python -c "import matplotlib; print(matplotlib.__file__)"
        ```
        (Note the path where Matplotlib is installed. It’s typically within your Python environment under lib/python3.x/site-packages/matplotlib.)
    
    4. Copy Fonts to Matplotlib's Font Directory

        You need to copy the Nanum fonts to Matplotlib's font directory so that it can be used for rendering Korean text.
        ```
        cd /home/[user]/miniconda3/lib/python3.10/site-packages/matplotlib/mpl-data/fonts/ttf
        ```
        Then, list the available Nanum fonts:
        ```
        ls -al /usr/share/fonts/truetype/nanum/
        ```
        Finally, copy the Nanum fonts to the Matplotlib fonts directory:
        ```
        cp /usr/share/fonts/truetype/nanum/Nanum* /home/[user]/miniconda3/lib/python3.10/site-packages/matplotlib/mpl-data/fonts/ttf/
        ```

    5. Clear Matplotlib's Font Cache

        Clear Matplotlib's font cache to ensure that the newly copied fonts are recognized by Matplotlib.   
        ```
        rm -rf ~/.cache/matplotlib/*
        ```
        This removes the old cache files, and Matplotlib will regenerate the font cache the next time it runs.

