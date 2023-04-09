"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[95203],{3905:(e,n,t)=>{t.d(n,{Zo:()=>m,kt:()=>u});var r=t(67294);function s(e,n,t){return n in e?Object.defineProperty(e,n,{value:t,enumerable:!0,configurable:!0,writable:!0}):e[n]=t,e}function a(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,r)}return t}function o(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?a(Object(t),!0).forEach((function(n){s(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):a(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}function c(e,n){if(null==e)return{};var t,r,s=function(e,n){if(null==e)return{};var t,r,s={},a=Object.keys(e);for(r=0;r<a.length;r++)t=a[r],n.indexOf(t)>=0||(s[t]=e[t]);return s}(e,n);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);for(r=0;r<a.length;r++)t=a[r],n.indexOf(t)>=0||Object.prototype.propertyIsEnumerable.call(e,t)&&(s[t]=e[t])}return s}var l=r.createContext({}),i=function(e){var n=r.useContext(l),t=n;return e&&(t="function"==typeof e?e(n):o(o({},n),e)),t},m=function(e){var n=i(e.components);return r.createElement(l.Provider,{value:n},e.children)},p={inlineCode:"code",wrapper:function(e){var n=e.children;return r.createElement(r.Fragment,{},n)}},d=r.forwardRef((function(e,n){var t=e.components,s=e.mdxType,a=e.originalType,l=e.parentName,m=c(e,["components","mdxType","originalType","parentName"]),d=i(t),u=s,_=d["".concat(l,".").concat(u)]||d[u]||p[u]||a;return t?r.createElement(_,o(o({ref:n},m),{},{components:t})):r.createElement(_,o({ref:n},m))}));function u(e,n){var t=arguments,s=n&&n.mdxType;if("string"==typeof e||s){var a=t.length,o=new Array(a);o[0]=d;var c={};for(var l in n)hasOwnProperty.call(n,l)&&(c[l]=n[l]);c.originalType=e,c.mdxType="string"==typeof e?e:s,o[1]=c;for(var i=2;i<a;i++)o[i]=t[i];return r.createElement.apply(null,o)}return r.createElement.apply(null,t)}d.displayName="MDXCreateElement"},24530:(e,n,t)=>{t.r(n),t.d(n,{assets:()=>l,contentTitle:()=>o,default:()=>p,frontMatter:()=>a,metadata:()=>c,toc:()=>i});var r=t(87462),s=(t(67294),t(3905));const a={},o="Reading data from MySQL in CSV and saving into S3",c={unversionedId:"assignments/mysql-s3-incremental/README",id:"assignments/mysql-s3-incremental/README",title:"Reading data from MySQL in CSV and saving into S3",description:"In this lab, we are loading the data from RDS MySQL Database into CSV and then saving that csv into S3 using Boto3.",source:"@site/docs/11-assignments/mysql-s3-incremental/README.md",sourceDirName:"11-assignments/mysql-s3-incremental",slug:"/assignments/mysql-s3-incremental/",permalink:"/docs/assignments/mysql-s3-incremental/",draft:!1,tags:[],version:"current",lastUpdatedBy:"sparsh",lastUpdatedAt:1681047270,formattedLastUpdatedAt:"Apr 9, 2023",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"Mistplay Data Engineer Take Home Challenge",permalink:"/docs/assignments/mistplay-takehome/"},next:{title:"OLX Data Engineering Challenge",permalink:"/docs/assignments/olx-python/"}},l={},i=[{value:"Batch mode",id:"batch-mode",level:2},{value:"Incremental mode",id:"incremental-mode",level:2}],m={toc:i};function p(e){let{components:n,...t}=e;return(0,s.kt)("wrapper",(0,r.Z)({},m,t,{components:n,mdxType:"MDXLayout"}),(0,s.kt)("h1",{id:"reading-data-from-mysql-in-csv-and-saving-into-s3"},"Reading data from MySQL in CSV and saving into S3"),(0,s.kt)("p",null,"In this lab, we are loading the data from RDS MySQL Database into CSV and then saving that csv into S3 using Boto3."),(0,s.kt)("p",null,"We are loading the data in batch as well as in incremental fashion."),(0,s.kt)("h2",{id:"batch-mode"},"Batch mode"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-py",metastring:'title="./src/extract_mysql_full.py"',title:'"./src/extract_mysql_full.py"'},'conn = pymysql.connect(host=hostname,\n    user=username,\n    password=password,\n    db=dbname,\n    port=int(port))\n\nm_query = "SELECT * FROM orders;"\nlocal_filename = "order_extracts.csv"\n\nm_cursor = conn.cursor()\nm_cursor.execute(m_query)\nresults = m_cursor.fetchall()\n\nwith open(local_filename, \'w\') as fp:\n    csv_w = csv.writer(fp, delimiter=\'|\')\n    csv_w.writerows(results)\n\nfp.close()\nm_cursor.close()\nconn.close()\n\n# load the aws_boto_credentials values:\nparser = configparser.ConfigParser()\nparser.read("pipeline.conf")\naccess_key = parser.get("aws_boto_credentials", "access_key")\nsecret_key = parser.get("aws_boto_credentials", "secret_key")\nbucket_name = parser.get("aws_boto_credentials", "bucket_name")\n\ns3 = boto3.client(\'s3\',\n    aws_access_key_id=access_key,\n    aws_secret_access_key=secret_key)\n\ns3_file = local_filename\n\ns3.upload_file(local_filename, bucket_name, s3_file)\n')),(0,s.kt)("h2",{id:"incremental-mode"},"Incremental mode"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-py",metastring:'title="./src/extract_mysql_incremental.py"',title:'"./src/extract_mysql_incremental.py"'},'rs_conn = psycopg2.connect(\n    "dbname=" + dbname\n    + " user=" + user\n    + " password=" + password\n    + " host=" + host\n    + " port=" + port\n)\n\nrs_sql = """ select coalesce(max(lastupdated), \n    \'1900-01-01\')\n    from orders;"""\nrs_cursor = rs_conn.cursor()\nrs_cursor.execute(rs_sql)\nresult = rs_cursor.fetchone()\n\n# There\'s only one row and column returned\nlast_updated_warehouse = result[0]\n\nrs_cursor.close()\nrs_conn.commit()\n\nconn = pymysql.connect(host=hostname,\n    user=username,\n    password=password,\n    db=dbname,\n    port=int(port))\n\nif conn is None:\n    print("Error connecting to the MySQL database")\nelse:\n    print("MySQL connection established!")\n\nm_query = """SELECT * \n    FROM orders\n    WHERE lastupdated > %s;"""\nlocal_filename = "order_extracts_incremental.csv"\n\nm_cursor = conn.cursor()\nm_cursor.execute(m_query, (last_updated_warehouse,))\nresults = m_cursor.fetchall()\n\nwith open(local_filename, \'w\') as fp:\n    csv_w = csv.writer(fp, delimiter=\'|\')\n    csv_w.writerows(results)\n\nfp.close()\nm_cursor.close()\nconn.close()\n\n# load the aws_boto_credentials values:\nparser = configparser.ConfigParser()\nparser.read("pipeline.conf")\naccess_key = parser.get("aws_boto_credentials", "access_key")\nsecret_key = parser.get("aws_boto_credentials", "secret_key")\nbucket_name = parser.get("aws_boto_credentials", "bucket_name")\n\ns3 = boto3.client(\'s3\',\n    aws_access_key_id=access_key,\n    aws_secret_access_key=secret_key)\n\ns3_file = local_filename\n\ns3.upload_file(local_filename, bucket_name, s3_file)\n')))}p.isMDXComponent=!0}}]);