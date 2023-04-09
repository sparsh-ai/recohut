"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[53444],{3905:(t,e,a)=>{a.d(e,{Zo:()=>s,kt:()=>u});var n=a(67294);function r(t,e,a){return e in t?Object.defineProperty(t,e,{value:a,enumerable:!0,configurable:!0,writable:!0}):t[e]=a,t}function o(t,e){var a=Object.keys(t);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(t);e&&(n=n.filter((function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable}))),a.push.apply(a,n)}return a}function l(t){for(var e=1;e<arguments.length;e++){var a=null!=arguments[e]?arguments[e]:{};e%2?o(Object(a),!0).forEach((function(e){r(t,e,a[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(a)):o(Object(a)).forEach((function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(a,e))}))}return t}function i(t,e){if(null==t)return{};var a,n,r=function(t,e){if(null==t)return{};var a,n,r={},o=Object.keys(t);for(n=0;n<o.length;n++)a=o[n],e.indexOf(a)>=0||(r[a]=t[a]);return r}(t,e);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(t);for(n=0;n<o.length;n++)a=o[n],e.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(t,a)&&(r[a]=t[a])}return r}var p=n.createContext({}),m=function(t){var e=n.useContext(p),a=e;return t&&(a="function"==typeof t?t(e):l(l({},e),t)),a},s=function(t){var e=m(t.components);return n.createElement(p.Provider,{value:e},t.children)},d={inlineCode:"code",wrapper:function(t){var e=t.children;return n.createElement(n.Fragment,{},e)}},c=n.forwardRef((function(t,e){var a=t.components,r=t.mdxType,o=t.originalType,p=t.parentName,s=i(t,["components","mdxType","originalType","parentName"]),c=m(a),u=r,h=c["".concat(p,".").concat(u)]||c[u]||d[u]||o;return a?n.createElement(h,l(l({ref:e},s),{},{components:a})):n.createElement(h,l({ref:e},s))}));function u(t,e){var a=arguments,r=e&&e.mdxType;if("string"==typeof t||r){var o=a.length,l=new Array(o);l[0]=c;var i={};for(var p in e)hasOwnProperty.call(e,p)&&(i[p]=e[p]);i.originalType=t,i.mdxType="string"==typeof t?t:r,l[1]=i;for(var m=2;m<o;m++)l[m]=a[m];return n.createElement.apply(null,l)}return n.createElement.apply(null,a)}c.displayName="MDXCreateElement"},55158:(t,e,a)=>{a.r(e),a.d(e,{assets:()=>p,contentTitle:()=>l,default:()=>d,frontMatter:()=>o,metadata:()=>i,toc:()=>m});var n=a(87462),r=(a(67294),a(3905));const o={},l="Apache Beam",i={unversionedId:"processing/apache-beam",id:"processing/apache-beam",title:"Apache Beam",description:"What is apache beam?",source:"@site/docs/03-processing/apache-beam.md",sourceDirName:"03-processing",slug:"/processing/apache-beam",permalink:"/docs/processing/apache-beam",draft:!1,tags:[],version:"current",lastUpdatedBy:"sparsh",lastUpdatedAt:1681047270,formattedLastUpdatedAt:"Apr 9, 2023",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"XML",permalink:"/docs/storage/xml"},next:{title:"Druid",permalink:"/docs/processing/apache-druid"}},p={},m=[{value:"What is apache beam?",id:"what-is-apache-beam",level:2},{value:"Python transform catalog overview",id:"python-transform-catalog-overview",level:2},{value:"Element-wise",id:"element-wise",level:3},{value:"Aggregation",id:"aggregation",level:3},{value:"Other",id:"other",level:3}],s={toc:m};function d(t){let{components:e,...a}=t;return(0,r.kt)("wrapper",(0,n.Z)({},s,a,{components:e,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"apache-beam"},"Apache Beam"),(0,r.kt)("h2",{id:"what-is-apache-beam"},"What is apache beam?"),(0,r.kt)("p",null,"Apache Beam is a library for parallel data processing. Beam is commonly used for Extract, Transform, and Load (ETL), batch, and stream processing. It does particularly well with large amounts of data since it can use mutliple machines to process everything at the same time."),(0,r.kt)("p",null,"Apache Beam comprises four basic features:"),(0,r.kt)("ol",null,(0,r.kt)("li",{parentName:"ol"},"Pipeline - Pipeline is responsible for reading, processing, and saving the data. This whole cycle is a pipeline starting from the input until its entire circle to output. Every Beam program is capable of generating a Pipeline."),(0,r.kt)("li",{parentName:"ol"},"PCollection - It is equivalent to RDD or DataFrames in Spark. The pipeline creates a PCollection by reading data from a data source, and after that, more PCollections keep on developing as PTransforms are applied to it."),(0,r.kt)("li",{parentName:"ol"},"PTransform - Each PTransform on PCollection results in a new PCollection making it immutable. Once constructed, you will not be able to configure individual items in a PCollection. A transformation onPCollection will result in a new PCollection. The features in a PCollection can be of any type, but all must be of the same kind. However, to maintain disseminated processing, Beam encodes each element as a byte string so that Beam can pass around items to distributed workers."),(0,r.kt)("li",{parentName:"ol"},"Runner - It determines where this pipeline will operate.")),(0,r.kt)("p",null,"In Beam, your data lives in a\xa0",(0,r.kt)("strong",{parentName:"p"},(0,r.kt)("inlineCode",{parentName:"strong"},"PCollection")),", which stands for\xa0",(0,r.kt)("em",{parentName:"p"},"Parallel Collection"),". A\xa0",(0,r.kt)("inlineCode",{parentName:"p"},"PCollection"),"\xa0is like a\xa0",(0,r.kt)("strong",{parentName:"p"},"list of elements"),", but without any order guarantees. This allows Beam to easily parallelize and distribute the\xa0",(0,r.kt)("inlineCode",{parentName:"p"},"PCollection"),"'s elements."),(0,r.kt)("p",null,(0,r.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/214567888-83bb1b64-45dd-41fb-b1bf-ba59abf8ed08.png",alt:null})),(0,r.kt)("p",null,"Once you have your data, the next step is to transform it. In Beam, you transform data using\xa0",(0,r.kt)("strong",{parentName:"p"},(0,r.kt)("inlineCode",{parentName:"strong"},"PTransform")),"s, which stands for\xa0",(0,r.kt)("em",{parentName:"p"},"Parallel Transform"),". A\xa0",(0,r.kt)("inlineCode",{parentName:"p"},"PTransform"),"\xa0is like a\xa0",(0,r.kt)("strong",{parentName:"p"},"function"),", they take some inputs, transform them and create some outputs."),(0,r.kt)("p",null,(0,r.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/214567899-4f8efbd8-2cc2-49b4-906f-dbc9045fc02e.png",alt:null})),(0,r.kt)("p",null,"We pass the elements from step1 through step3 and save the results into ",(0,r.kt)("inlineCode",{parentName:"p"},"outputs"),"."),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-py"},"outputs = pipeline | step1 | step2 | step3\n")),(0,r.kt)("p",null,"This is equivalent to the example above."),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-py"},"outputs = (\n  pipeline\n  | step1\n  | step2\n  | step3\n)\n")),(0,r.kt)("p",null,"Also, Beam expects each transform, or step, to have a unique\xa0",(0,r.kt)("em",{parentName:"p"},"label"),", or description. This makes it a lot easier to debug, and it's in general a good practice to start. You can use the\xa0",(0,r.kt)("em",{parentName:"p"},"right shift operator"),"\xa0",(0,r.kt)("inlineCode",{parentName:"p"},">>"),"\xa0to add a label to your transforms, like\xa0",(0,r.kt)("inlineCode",{parentName:"p"},"'My description' >> MyTransform"),"."),(0,r.kt)("p",null,"Try to give short but descriptive labels."),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-py"},"outputs = (\n  pipeline\n  | 'First step' >> step1\n  | 'Second step' >> step2\n  | 'Third step' >> step3\n)\n")),(0,r.kt)("h2",{id:"python-transform-catalog-overview"},"Python transform catalog overview"),(0,r.kt)("h3",{id:"element-wise"},"Element-wise"),(0,r.kt)("table",null,(0,r.kt)("thead",{parentName:"table"},(0,r.kt)("tr",{parentName:"thead"},(0,r.kt)("th",{parentName:"tr",align:null},"Transform"),(0,r.kt)("th",{parentName:"tr",align:null},"Description"))),(0,r.kt)("tbody",{parentName:"table"},(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("a",{parentName:"td",href:"https://beam.apache.org/documentation/transforms/python/elementwise/filter"},"Filter")),(0,r.kt)("td",{parentName:"tr",align:null},"Given a predicate, filter out all elements that don't satisfy the predicate.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("a",{parentName:"td",href:"https://beam.apache.org/documentation/transforms/python/elementwise/flatmap"},"FlatMap")),(0,r.kt)("td",{parentName:"tr",align:null},"Applies a function that returns a collection to every element in the input and outputs all resulting elements.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("a",{parentName:"td",href:"https://beam.apache.org/documentation/transforms/python/elementwise/keys"},"Keys")),(0,r.kt)("td",{parentName:"tr",align:null},"Extracts the key from each element in a collection of key-value pairs.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("a",{parentName:"td",href:"https://beam.apache.org/documentation/transforms/python/elementwise/kvswap"},"KvSwap")),(0,r.kt)("td",{parentName:"tr",align:null},"Swaps the key and value of each element in a collection of key-value pairs.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("a",{parentName:"td",href:"https://beam.apache.org/documentation/transforms/python/elementwise/map"},"Map")),(0,r.kt)("td",{parentName:"tr",align:null},"Applies a function to every element in the input and outputs the result.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("a",{parentName:"td",href:"https://beam.apache.org/documentation/transforms/python/elementwise/pardo"},"ParDo")),(0,r.kt)("td",{parentName:"tr",align:null},"The most-general mechanism for applying a user-defined ",(0,r.kt)("inlineCode",{parentName:"td"},"DoFn"),"\xa0to every element in the input collection.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("a",{parentName:"td",href:"https://beam.apache.org/documentation/transforms/python/elementwise/partition"},"Partition")),(0,r.kt)("td",{parentName:"tr",align:null},"Routes each input element to a specific output collection based on some partition function.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("a",{parentName:"td",href:"https://beam.apache.org/documentation/transforms/python/elementwise/regex"},"Regex")),(0,r.kt)("td",{parentName:"tr",align:null},"Filters input string elements based on a regex. May also transform them based on the matching groups.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("a",{parentName:"td",href:"https://beam.apache.org/documentation/transforms/python/elementwise/reify"},"Reify")),(0,r.kt)("td",{parentName:"tr",align:null},"Transforms for converting between explicit and implicit form of various Beam values.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("a",{parentName:"td",href:"https://beam.apache.org/documentation/transforms/python/elementwise/runinference"},"RunInference")),(0,r.kt)("td",{parentName:"tr",align:null},"Uses machine learning (ML) models to do local and remote inference.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("a",{parentName:"td",href:"https://beam.apache.org/documentation/transforms/python/elementwise/tostring"},"ToString")),(0,r.kt)("td",{parentName:"tr",align:null},"Transforms every element in an input collection a string.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("a",{parentName:"td",href:"https://beam.apache.org/documentation/transforms/python/elementwise/withtimestamps"},"WithTimestamps")),(0,r.kt)("td",{parentName:"tr",align:null},"Applies a function to determine a timestamp to each element in the output collection, and updates the implicit timestamp associated with each input. Note that it is only safe to adjust timestamps forwards.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("a",{parentName:"td",href:"https://beam.apache.org/documentation/transforms/python/elementwise/values"},"Values")),(0,r.kt)("td",{parentName:"tr",align:null},"Extracts the value from each element in a collection of key-value pairs.")))),(0,r.kt)("h3",{id:"aggregation"},"Aggregation"),(0,r.kt)("table",null,(0,r.kt)("thead",{parentName:"table"},(0,r.kt)("tr",{parentName:"thead"},(0,r.kt)("th",{parentName:"tr",align:null},"Transform"),(0,r.kt)("th",{parentName:"tr",align:null},"Description"))),(0,r.kt)("tbody",{parentName:"table"},(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"ApproximateQuantiles"),(0,r.kt)("td",{parentName:"tr",align:null},"Not available. See",(0,r.kt)("a",{parentName:"td",href:"https://issues.apache.org/jira/browse/BEAM-6694"},"BEAM-6694"),"\xa0for updates.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"ApproximateUnique"),(0,r.kt)("td",{parentName:"tr",align:null},"Not available. See",(0,r.kt)("a",{parentName:"td",href:"https://issues.apache.org/jira/browse/BEAM-6693"},"BEAM-6693"),"\xa0for updates.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("a",{parentName:"td",href:"https://beam.apache.org/documentation/transforms/python/aggregation/cogroupbykey"},"CoGroupByKey")),(0,r.kt)("td",{parentName:"tr",align:null},"Takes several keyed collections of elements and produces a collection where each element consists of a key and all values associated with that key.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("a",{parentName:"td",href:"https://beam.apache.org/documentation/transforms/python/aggregation/combineglobally"},"CombineGlobally")),(0,r.kt)("td",{parentName:"tr",align:null},"Transforms to combine elements.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("a",{parentName:"td",href:"https://beam.apache.org/documentation/transforms/python/aggregation/combineperkey"},"CombinePerKey")),(0,r.kt)("td",{parentName:"tr",align:null},"Transforms to combine elements for each key.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("a",{parentName:"td",href:"https://beam.apache.org/documentation/transforms/python/aggregation/combinevalues"},"CombineValues")),(0,r.kt)("td",{parentName:"tr",align:null},"Transforms to combine keyed iterables.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"CombineWithContext"),(0,r.kt)("td",{parentName:"tr",align:null},"Not available.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("a",{parentName:"td",href:"https://beam.apache.org/documentation/transforms/python/aggregation/count"},"Count")),(0,r.kt)("td",{parentName:"tr",align:null},"Counts the number of elements within each aggregation.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("a",{parentName:"td",href:"https://beam.apache.org/documentation/transforms/python/aggregation/distinct"},"Distinct")),(0,r.kt)("td",{parentName:"tr",align:null},"Produces a collection containing distinct elements from the input collection.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("a",{parentName:"td",href:"https://beam.apache.org/documentation/transforms/python/aggregation/groupbykey"},"GroupByKey")),(0,r.kt)("td",{parentName:"tr",align:null},"Takes a keyed collection of elements and produces a collection where each element consists of a key and all values associated with that key.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("a",{parentName:"td",href:"https://beam.apache.org/documentation/transforms/python/aggregation/groupby"},"GroupBy")),(0,r.kt)("td",{parentName:"tr",align:null},"Takes a collection of elements and produces a collection grouped, by properties of those elements. Unlike GroupByKey, the key is dynamically created from the elements themselves.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("a",{parentName:"td",href:"https://beam.apache.org/documentation/transforms/python/aggregation/groupintobatches"},"GroupIntoBatches")),(0,r.kt)("td",{parentName:"tr",align:null},"Batches the input into desired batch size.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("a",{parentName:"td",href:"https://beam.apache.org/documentation/transforms/python/aggregation/latest"},"Latest")),(0,r.kt)("td",{parentName:"tr",align:null},"Gets the element with the latest timestamp.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("a",{parentName:"td",href:"https://beam.apache.org/documentation/transforms/python/aggregation/max"},"Max")),(0,r.kt)("td",{parentName:"tr",align:null},"Gets the element with the maximum value within each aggregation.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("a",{parentName:"td",href:"https://beam.apache.org/documentation/transforms/python/aggregation/mean"},"Mean")),(0,r.kt)("td",{parentName:"tr",align:null},"Computes the average within each aggregation.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("a",{parentName:"td",href:"https://beam.apache.org/documentation/transforms/python/aggregation/min"},"Min")),(0,r.kt)("td",{parentName:"tr",align:null},"Gets the element with the minimum value within each aggregation.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("a",{parentName:"td",href:"https://beam.apache.org/documentation/transforms/python/aggregation/sample"},"Sample")),(0,r.kt)("td",{parentName:"tr",align:null},"Randomly select some number of elements from each aggregation.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("a",{parentName:"td",href:"https://beam.apache.org/documentation/transforms/python/aggregation/sum"},"Sum")),(0,r.kt)("td",{parentName:"tr",align:null},"Sums all the elements within each aggregation.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("a",{parentName:"td",href:"https://beam.apache.org/documentation/transforms/python/aggregation/top"},"Top")),(0,r.kt)("td",{parentName:"tr",align:null},"Compute the largest element(s) in each aggregation.")))),(0,r.kt)("h3",{id:"other"},"Other"),(0,r.kt)("table",null,(0,r.kt)("thead",{parentName:"table"},(0,r.kt)("tr",{parentName:"thead"},(0,r.kt)("th",{parentName:"tr",align:null},"Transform"),(0,r.kt)("th",{parentName:"tr",align:null},"Description"))),(0,r.kt)("tbody",{parentName:"table"},(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("a",{parentName:"td",href:"https://beam.apache.org/documentation/transforms/python/other/create"},"Create")),(0,r.kt)("td",{parentName:"tr",align:null},"Creates a collection from an in-memory list.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("a",{parentName:"td",href:"https://beam.apache.org/documentation/transforms/python/other/flatten"},"Flatten")),(0,r.kt)("td",{parentName:"tr",align:null},"Given multiple input collections, produces a single output collection containing all elements from all of the input collections.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"PAssert"),(0,r.kt)("td",{parentName:"tr",align:null},"Not available.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("a",{parentName:"td",href:"https://beam.apache.org/documentation/transforms/python/other/reshuffle"},"Reshuffle")),(0,r.kt)("td",{parentName:"tr",align:null},"Given an input collection, redistributes the elements between workers. This is most useful for adjusting parallelism or preventing coupled failures.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"View"),(0,r.kt)("td",{parentName:"tr",align:null},"Not available.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("a",{parentName:"td",href:"https://beam.apache.org/documentation/transforms/python/other/windowinto"},"WindowInto")),(0,r.kt)("td",{parentName:"tr",align:null},"Logically divides up or groups the elements of a collection into finite windows according to a function.")))),(0,r.kt)("p",null,"Refer to ",(0,r.kt)("a",{parentName:"p",href:"https://beam.apache.org/documentation/transforms/python/overview/"},"this")," documentation for up-to-date list."))}d.isMDXComponent=!0}}]);