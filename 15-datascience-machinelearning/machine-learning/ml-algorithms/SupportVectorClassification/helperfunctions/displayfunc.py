# import pandas, numpy, and matplotlib
from sklearn.inspection import DecisionBoundaryDisplay

def dispbound(model, X, xvarnames, y, title):
  dispfit = model.fit(X,y)
  disp = DecisionBoundaryDisplay.from_estimator(
    dispfit, X, response_method="predict",
    xlabel=xvarnames[0], ylabel=xvarnames[1],
    alpha=0.5,
  )
  scatter = disp.ax_.scatter(X[:,0], X[:,1],
    c=y, edgecolor="k")
  
  disp.ax_.set_title(title)
  #disp.ax_.set_xlim([-0.25, 1.25])
  #disp.ax_.set_ylim([-0.25, 1.25])
  legend1 = disp.ax_.legend(*scatter.legend_elements(),
    loc="lower left", title="Home Win")
  disp.ax_.add_artist(legend1)



