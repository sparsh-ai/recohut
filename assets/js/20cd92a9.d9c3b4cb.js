"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[12169],{3905:(e,r,t)=>{t.d(r,{Zo:()=>c,kt:()=>u});var n=t(67294);function o(e,r,t){return r in e?Object.defineProperty(e,r,{value:t,enumerable:!0,configurable:!0,writable:!0}):e[r]=t,e}function a(e,r){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);r&&(n=n.filter((function(r){return Object.getOwnPropertyDescriptor(e,r).enumerable}))),t.push.apply(t,n)}return t}function s(e){for(var r=1;r<arguments.length;r++){var t=null!=arguments[r]?arguments[r]:{};r%2?a(Object(t),!0).forEach((function(r){o(e,r,t[r])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):a(Object(t)).forEach((function(r){Object.defineProperty(e,r,Object.getOwnPropertyDescriptor(t,r))}))}return e}function l(e,r){if(null==e)return{};var t,n,o=function(e,r){if(null==e)return{};var t,n,o={},a=Object.keys(e);for(n=0;n<a.length;n++)t=a[n],r.indexOf(t)>=0||(o[t]=e[t]);return o}(e,r);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);for(n=0;n<a.length;n++)t=a[n],r.indexOf(t)>=0||Object.prototype.propertyIsEnumerable.call(e,t)&&(o[t]=e[t])}return o}var i=n.createContext({}),p=function(e){var r=n.useContext(i),t=r;return e&&(t="function"==typeof e?e(r):s(s({},r),e)),t},c=function(e){var r=p(e.components);return n.createElement(i.Provider,{value:r},e.children)},d={inlineCode:"code",wrapper:function(e){var r=e.children;return n.createElement(n.Fragment,{},r)}},m=n.forwardRef((function(e,r){var t=e.components,o=e.mdxType,a=e.originalType,i=e.parentName,c=l(e,["components","mdxType","originalType","parentName"]),m=p(t),u=o,y=m["".concat(i,".").concat(u)]||m[u]||d[u]||a;return t?n.createElement(y,s(s({ref:r},c),{},{components:t})):n.createElement(y,s({ref:r},c))}));function u(e,r){var t=arguments,o=r&&r.mdxType;if("string"==typeof e||o){var a=t.length,s=new Array(a);s[0]=m;var l={};for(var i in r)hasOwnProperty.call(r,i)&&(l[i]=r[i]);l.originalType=e,l.mdxType="string"==typeof e?e:o,s[1]=l;for(var p=2;p<a;p++)s[p]=t[p];return n.createElement.apply(null,s)}return n.createElement.apply(null,t)}m.displayName="MDXCreateElement"},56240:(e,r,t)=>{t.r(r),t.d(r,{assets:()=>i,contentTitle:()=>s,default:()=>d,frontMatter:()=>a,metadata:()=>l,toc:()=>p});var n=t(87462),o=(t(67294),t(3905));const a={},s="Regression",l={unversionedId:"datascience/regression/README",id:"datascience/regression/README",title:"Regression",description:"Sklearn Regression Model",source:"@site/docs/10-datascience/regression/README.md",sourceDirName:"10-datascience/regression",slug:"/datascience/regression/",permalink:"/docs/datascience/regression/",draft:!1,tags:[],version:"current",lastUpdatedBy:"sparsh",lastUpdatedAt:1681047270,formattedLastUpdatedAt:"Apr 9, 2023",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"Recommender System with Node2vec Graph Embeddings",permalink:"/docs/datascience/recsys/movielens-mf-node2vec-graph-embeddings/"},next:{title:"Experimentation",permalink:"/docs/datascience/reinforcement-learning/"}},i={},p=[{value:"Sklearn Regression Model",id:"sklearn-regression-model",level:2},{value:"Keras Regression Model",id:"keras-regression-model",level:2}],c={toc:p};function d(e){let{components:r,...t}=e;return(0,o.kt)("wrapper",(0,n.Z)({},c,t,{components:r,mdxType:"MDXLayout"}),(0,o.kt)("h1",{id:"regression"},"Regression"),(0,o.kt)("h2",{id:"sklearn-regression-model"},"Sklearn Regression Model"),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-py"},"from sklearn.neural_network import MLPRegressor\nfrom sklearn.metrics import mean_squared_error\n\nregr = MLPRegressor(random_state=1, max_iter=10000, hidden_layer_sizes=(64,32, 16, 8),activation='relu',momentum=0.9).fit(X_train, y_train)\n\nregr.score(X_test, y_test)\n\nmean_squared_error(y_test, regr.predict(X_test), squared=False)\n\npd.DataFrame(regr.loss_curve_).plot()\n")),(0,o.kt)("h2",{id:"keras-regression-model"},"Keras Regression Model"),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-py"},'import tensorflow as tf\nfrom tensorflow import keras\nfrom keras import backend as K\n\nimport os\nfrom keras.models import Sequential\nfrom keras.layers import Dense\n\n%reload_ext tensorboard\n\nos.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"\nos.environ["CUDA_VISIBLE_DEVICES"] = ""\n\nseed = 1\ntf.keras.utils.set_random_seed(\n    seed\n)\n')),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-py"},"# def r_square(y_true, y_pred):\n#     SS_res =  K.sum(K.square( y_true-y_pred )) \n#     SS_tot = K.sum(K.square( y_true - K.mean(y_true) ) ) \n#     return ( 1 - SS_res/(SS_tot + K.epsilon()) )\n\nmodel = Sequential()\nmodel.add(Dense(64, input_dim=3, activation='relu'))\nmodel.add(keras.layers.Dropout(0.4))\nmodel.add(Dense(32, activation='relu'))\nmodel.add(keras.layers.Dropout(0.4))\n# model.add(Dense(16, activation='relu'))\nmodel.add(Dense(8, activation='relu'))\nmodel.add(Dense(1, activation='linear'))\nopt = tf.keras.optimizers.Adam(learning_rate=0.001)\nes_callback = keras.callbacks.EarlyStopping(monitor='val_loss', patience=5, mode='min')\n# model.compile(optimizer=opt, loss='mean_squared_error', metrics=['mae', r_square])\nmodel.compile(optimizer=opt, loss='mean_squared_error', metrics=['mae'])\n\nhistory = model.fit(X_train,\n                    y_train,\n                    epochs=100,\n                    batch_size=32,\n                    validation_data=(X_test, y_test),\n                    callbacks=[es_callback])\n")),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-py"},"# list all data in history\nprint(history.history.keys())\n\n# summarize history for mae\nplt.plot(history.history['mae'])\nplt.plot(history.history['val_mae'])\nplt.title('model Mean Absolute Error (MAE)')\nplt.ylabel('MAE')\nplt.xlabel('epoch')\nplt.legend(['train', 'test'], loc='upper left')\nplt.show()\n\n# # summarize history for R2\n# plt.plot(history.history['r_square'])\n# plt.plot(history.history['val_r_square'])\n# plt.title('model Accuracy (R2)')\n# plt.ylabel('R2')\n# plt.xlabel('epoch')\n# plt.legend(['train', 'test'], loc='upper left')\n# plt.show()\n\n# summarize history for loss\nplt.plot(history.history['loss'])\nplt.plot(history.history['val_loss'])\nplt.title('model loss')\nplt.ylabel('loss')\nplt.xlabel('epoch')\nplt.legend(['train', 'test'], loc='upper left')\nplt.show()\n\nfrom sklearn.metrics import mean_squared_error\nmean_squared_error(y_test, model.predict(X_test), squared=False)\n\nfrom sklearn.metrics import r2_score\nbaseline_model_score = r2_score(y_test, model.predict(X_test))\nbaseline_model_score\n")))}d.isMDXComponent=!0}}]);