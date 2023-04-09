"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[65356],{3905:(e,t,r)=>{r.d(t,{Zo:()=>c,kt:()=>m});var a=r(67294);function o(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function n(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);t&&(a=a.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,a)}return r}function s(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?n(Object(r),!0).forEach((function(t){o(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):n(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function i(e,t){if(null==e)return{};var r,a,o=function(e,t){if(null==e)return{};var r,a,o={},n=Object.keys(e);for(a=0;a<n.length;a++)r=n[a],t.indexOf(r)>=0||(o[r]=e[r]);return o}(e,t);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);for(a=0;a<n.length;a++)r=n[a],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(o[r]=e[r])}return o}var l=a.createContext({}),p=function(e){var t=a.useContext(l),r=t;return e&&(r="function"==typeof e?e(t):s(s({},t),e)),r},c=function(e){var t=p(e.components);return a.createElement(l.Provider,{value:t},e.children)},u={inlineCode:"code",wrapper:function(e){var t=e.children;return a.createElement(a.Fragment,{},t)}},d=a.forwardRef((function(e,t){var r=e.components,o=e.mdxType,n=e.originalType,l=e.parentName,c=i(e,["components","mdxType","originalType","parentName"]),d=p(r),m=o,g=d["".concat(l,".").concat(m)]||d[m]||u[m]||n;return r?a.createElement(g,s(s({ref:t},c),{},{components:r})):a.createElement(g,s({ref:t},c))}));function m(e,t){var r=arguments,o=t&&t.mdxType;if("string"==typeof e||o){var n=r.length,s=new Array(n);s[0]=d;var i={};for(var l in t)hasOwnProperty.call(t,l)&&(i[l]=t[l]);i.originalType=e,i.mdxType="string"==typeof e?e:o,s[1]=i;for(var p=2;p<n;p++)s[p]=r[p];return a.createElement.apply(null,s)}return a.createElement.apply(null,r)}d.displayName="MDXCreateElement"},85105:(e,t,r)=>{r.r(t),r.d(t,{assets:()=>l,contentTitle:()=>s,default:()=>u,frontMatter:()=>n,metadata:()=>i,toc:()=>p});var a=r(87462),o=(r(67294),r(3905));const n={},s="Stored Procedures",i={unversionedId:"foundations/programming-languages/sql/stored-procedures",id:"foundations/programming-languages/sql/stored-procedures",title:"Stored Procedures",description:"A\xa0stored procedure\xa0is a\xa0set of SQL statements\xa0stored in a database. These statements can request data entry parameters, which are used as variables during execution, and can constitute a\xa0data output.",source:"@site/docs/01-foundations/04-programming-languages/sql/stored-procedures.md",sourceDirName:"01-foundations/04-programming-languages/sql",slug:"/foundations/programming-languages/sql/stored-procedures",permalink:"/docs/foundations/programming-languages/sql/stored-procedures",draft:!1,tags:[],version:"current",lastUpdatedBy:"sparsh",lastUpdatedAt:1681047270,formattedLastUpdatedAt:"Apr 9, 2023",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"SQL Query",permalink:"/docs/foundations/programming-languages/sql/sql-query"},next:{title:"SQL String Functions",permalink:"/docs/foundations/programming-languages/sql/string-functions"}},l={},p=[],c={toc:p};function u(e){let{components:t,...r}=e;return(0,o.kt)("wrapper",(0,a.Z)({},c,r,{components:t,mdxType:"MDXLayout"}),(0,o.kt)("h1",{id:"stored-procedures"},"Stored Procedures"),(0,o.kt)("p",null,"A\xa0",(0,o.kt)("em",{parentName:"p"},"stored procedure"),"\xa0is a\xa0set of SQL statements\xa0stored in a database. These statements can request data entry parameters, which are used as variables during execution, and can constitute a\xa0data output."),(0,o.kt)("p",null,"In the following\xa0example, we can see the creation of a\xa0",(0,o.kt)("em",{parentName:"p"},"stored SQL procedure"),"\xa0called\xa0",(0,o.kt)("strong",{parentName:"p"},"All_Customers"),", which requests two variables,\xa0",(0,o.kt)("strong",{parentName:"p"},"City"),"\xa0and\xa0",(0,o.kt)("strong",{parentName:"p"},"PostalCode"),", to filter the results in\xa0the query:"),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-sql"},"CREATE PROCEDURE All_Customers\n@City nvarchar(30), @PostalCode nvarchar(10)\nAS\nSELECT * FROM Customers WHERE City = @City AND PostalCode = @PostalCode\nGO;\n")),(0,o.kt)("p",null,"Objects\xa0in a\xa0database need a trigger to be called and start executing. For this reason, there is an object in relational databases called a\xa0",(0,o.kt)("em",{parentName:"p"},"trigger"),". Let's analyze\xa0it now."),(0,o.kt)("p",null,"If you want to save your SQL query on the database server for execution later, one way to do it is to use a stored procedure."),(0,o.kt)("p",null,"The first time you invoke a stored procedure, MySQL looks up for the name in the database catalog, compiles the stored procedure's code, place it in a memory area known as a cache, and execute the stored procedure."),(0,o.kt)("p",null,"If you invoke the same stored procedure in the same session again, MySQL just executes the stored procedure from the cache without having to recompile it."),(0,o.kt)("p",null,"A stored procedure can have\xa0",(0,o.kt)("a",{parentName:"p",href:"https://www.mysqltutorial.org/stored-procedures-parameters.aspx"},"parameters"),"\xa0so you can pass values to it and get the result back. For example, you can have a stored procedure that returns customers by country and city. In this case, the country and city are parameters of the stored procedure."),(0,o.kt)("p",null,"A stored procedure may contain control flow statements such as\xa0",(0,o.kt)("a",{parentName:"p",href:"https://www.mysqltutorial.org/mysql-if-statement/"},"IF"),",\xa0",(0,o.kt)("a",{parentName:"p",href:"https://www.mysqltutorial.org/mysql-case-statement/"},"CASE"),", and\xa0",(0,o.kt)("inlineCode",{parentName:"p"},"LOOP"),"\xa0that allow you to implement the code in the procedural way."),(0,o.kt)("p",null,"A stored procedure can call other stored procedures or\xa0",(0,o.kt)("a",{parentName:"p",href:"https://www.mysqltutorial.org/mysql-stored-function/"},"stored functions"),", which allows you to modulize your code."),(0,o.kt)("p",null,"Typically, a stored procedure contains multiple statements separated by semicolons (;). To compile the whole stored procedure as a single compound statement, you need to temporarily change the delimiter from the semicolon (;) to another delimiter such as\xa0",(0,o.kt)("inlineCode",{parentName:"p"},"$$"),"\xa0or\xa0",(0,o.kt)("inlineCode",{parentName:"p"},"//"),"."),(0,o.kt)("p",null,(0,o.kt)("strong",{parentName:"p"},"MySQL stored procedures advantages")),(0,o.kt)("p",null,"The following are the advantages of stored procedures."),(0,o.kt)("ol",null,(0,o.kt)("li",{parentName:"ol"},"Reduce network traffic - Stored procedures help reduce the network traffic between applications and MySQL Server. Because instead of sending multiple lengthy SQL statements, applications have to send only the name and parameters of stored procedures."),(0,o.kt)("li",{parentName:"ol"},"Centralize business logic in the database - You can use the stored procedures to implement business logic that is reusable by multiple applications. The stored procedures help reduce the efforts of duplicating the same logic in many applications and make your database more consistent."),(0,o.kt)("li",{parentName:"ol"},"Make database more secure - The database administrator can grant appropriate privileges to applications that only access specific stored procedures without giving any privileges on the underlying tables.")),(0,o.kt)("p",null,(0,o.kt)("strong",{parentName:"p"},"MySQL stored procedures disadvantages")),(0,o.kt)("p",null,"Besides those advantages, stored procedures also have disadvantages:"),(0,o.kt)("ol",null,(0,o.kt)("li",{parentName:"ol"},"Resource usages - If you use many stored procedures, the memory usage of every connection will increase substantially. Besides, overusing a large number of logical operations in the stored procedures will increase the CPU usage because the MySQL is not well-designed for logical operations."),(0,o.kt)("li",{parentName:"ol"},"Troubleshooting - It's difficult to debug stored procedures. Unfortunately, MySQL does not provide any facilities to debug stored procedures like other enterprise database products such as Oracle and SQL Server."),(0,o.kt)("li",{parentName:"ol"},"Maintenances - Developing and maintaining stored procedures often requires a specialized skill set that not all application developers possess. This may lead to problems in both application development and maintenance.")))}u.isMDXComponent=!0}}]);