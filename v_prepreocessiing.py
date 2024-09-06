import pydicom
import numpy as np
import matplotlib.pyplot as plt

def dicom_to_png_grid(axial_dicom_path, coronal_dicom_path, sagittal_dicom_path, output_path):
    axial_dicom = pydicom.dcmread(axial_dicom_path)
    coronal_dicom = pydicom.dcmread(coronal_dicom_path)
    sagittal_dicom = pydicom.dcmread(sagittal_dicom_path)
    
    axial_view = axial_dicom.pixel_array
    coronal_view = coronal_dicom.pixel_array
    sagittal_view = sagittal_dicom.pixel_array

    def normalize(arr):
        arr_min = arr.min()
        arr_max = arr.max()
        arr = (arr - arr_min) / (arr_max - arr_min) * 255
        return arr.astype(np.uint8)

    axial_view = normalize(axial_view)
    coronal_view = normalize(coronal_view)
    sagittal_view = normalize(sagittal_view)

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    axes[0].imshow(axial_view, cmap='gray')
    axes[0].set_title('Axial View')
    axes[0].axis('off')
    axes[1].imshow(coronal_view, cmap='gray')
    axes[1].set_title('Coronal View')
    axes[1].axis('off')
    axes[2].imshow(sagittal_view, cmap='gray')
    axes[2].set_title('Sagittal View')
    axes[2].axis('off')

    plt.savefig(output_path, bbox_inches='tight', pad_inches=0)
    plt.close()


axial_dicom_path = 'Dicom/DICOM_PA0_ST0_SE16_IM0'
coronal_dicom_path = 'Dicom/DICOM_PA0_ST0_SE16_IM1'
sagittal_dicom_path = 'Dicom/DICOM_PA0_ST0_SE16_IM2'

output_path = 'image.png'

dicom_to_png_grid(axial_dicom_path, coronal_dicom_path, sagittal_dicom_path, output_path)