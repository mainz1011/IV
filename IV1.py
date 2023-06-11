from bokeh.plotting import figure, output_file, show, save
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.transform import factor_cmap
from bokeh.palettes import Pastel1_9
import pandas

# Read in csv
df = pandas.read_csv('IV2022-Task3-Yin_(Sophie)Hui_original_data.csv')

# Create ColumnDataSource from dataframe (df)
source = ColumnDataSource(df)

output_file('test.html')

# Create a dog breed list using the method tolist 
dog_breed_list = source.data['Dog_Breed'].tolist()

# Add plot
p = figure (
    y_range=dog_breed_list,
    plot_width=800,
    plot_height=600,
    title='The Average Age of Different Dog Breeds',
    x_axis_label='Average Age (in years)',
    tools="pan, box_select, zoom_in, zoom_out, save" 
)

# render glyph
p.hbar(
    y='Dog_Breed',
    right='Average_Age',
    left=0,
    height=0.4,
    fill_color=factor_cmap(
        'Dog_Breed',
        palette=Pastel1_9,
        factors=dog_breed_list
    ),
    fill_alpha=0.9,
    source=source,
    legend_field='Dog_Breed'
)

# Add legend
p.legend.orientation='vertical'
p.legend.location='top_right'
p.legend.label_text_font_size='10px'

# Add Tooltips
hover = HoverTool()
hover.tooltips = """
  <div>
    <h4>@Dog_Breed</h4>
    <div><strong>Price: </strong>@Price <strong>Average Age: </strong>@Average_Age</div>
    <div><strong>Grown Dog Average Weight (lbs): Male </strong>@Grown_Male_Dog_Average_Weight_lbs<strong>; Female </strong>@Grown_Female_Dog_Average_Weight_lbs</div>
    <div><img src="@Image" alt="" width="100" height="70"/></div>
  </div>
"""

# Enable hover
p.add_tools(hover)

# Show results
show(p)

# Save file
save(p)