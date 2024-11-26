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
        under '/home/[user]/miniconda3/envs/[name]/lib/[python version]'
        cd ./site-packages/matplotlib/mpl-data/fonts/ttf
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

    6. (KOR) 또 다른 방법

        또 다른 방법은 matplotlib에서 한글 폰트의 경로를 명시적으로 지정해주는 방법. NanumGothic을 사용할 수 있도록 폰트 경로를 지정하는 방법을 설명해요. (시도는 안했는데, 간단해서 작동했으면 해요)
        ```
        import matplotlib.pyplot as plt
        from matplotlib import rcParams
        import matplotlib.font_manager as fm

        # NanumGothic 폰트 경로를 확인하고 설정합니다.
        font_path = "/usr/share/fonts/truetype/nanum/NanumGothic.ttf"
        font_prop = fm.FontProperties(fname=font_path)

        # 폰트 설정
        rcParams['font.family'] = font_prop.get_name()

        # 예시 그래프
        plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
        plt.title("한글 포함된 예시 그래프")
        plt.show()
        ```
