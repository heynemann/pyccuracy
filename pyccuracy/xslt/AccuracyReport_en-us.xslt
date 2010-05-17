<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:msxsl="urn:schemas-microsoft-com:xslt" exclude-result-prefixes="msxsl"
>
  <xsl:output method="html" indent="yes"/>

  <xsl:template match="/">
    <html>
      <head>
        <title>
            Pyccuracy - Tests Run Report -
            <span class="date">
              <xsl:value-of select ="@date"/>
            </span>
        </title>
        <style>
          <![CDATA[
          .header
          {
          font-size: medium;
          font-family: Helvetica;
          }
          td.header
          {
          background-color: #dedede;
          border: solid 1px black;
          height: 23px;
          }
          .footer
          {
          font-size: xx-small;
          font-family: Helvetica;
          }
          td.footer
          {
          background-color: #dedede;
          border: solid 1px black;
          height: 23px;
          }
          .date
          {
          color: dimgray;
          }
          .report
          {
          font-size: x-small;
          font-family: Helvetica;
          }
          td.report
          {
          border-left: solid 1px black;
          border-right: solid 1px black;
          border-top: solid 0px black;
          border-bottom: solid 0px black;
          }
          .runFailed
          {
          font-size: small;
          font-weight: bold;
          color: red;
          }
          .runSucceeded
          {
          font-size: small;
          font-weight: bold;
          color: darkgreen;
          }
          .summary
          {
          font-size: x-small;
          font-family: Helvetica;
          }
          td.summary
          {
          background-color: lightblue;
          border: dashed 1px dimgray;
          }
          .storiesHeader
          {
          font-size: small;
          font-weight: bold;
          font-family: Helvetica;
          }
          td.storiesHeader
          {
          background-color: lightGreen;
          }
          .storiesBody
          {
          font-size: x-small;
          font-family: Helvetica;
          }
          td.storiesBody
          {
          border-top: solid 1px lightGreen;
          border-bottom: solid 2px lightGreen;
          border-left: solid 2px lightGreen;
          border-right: solid 2px lightGreen;
          padding: 6px 6px 6px 6px;
          }
          .successfulTests
          {
          color: darkgreen;
          }
          .failedTests
          {
          color: red;
          }
          .condition
          {
          font-size: x-small;
          padding-left: 15px;
          }
          .action
          {
          font-size: x-small;
          padding-left: 30px;
          }
          .actionTime
          {
          font-size: x-small;
          color: Navy;
          }
          .odd
          {
          background-color: #dedede;
          height: 18px;
          }
          .even
          {
          background-color: white;
          height: 18px;
          }
          .totalTime
          {
          background-color: dimgray;
          color: White;
          font-size:x-small;
          height: 18px;
          }
          .totalTimeFinishTime
          {
          color: lightblue;
          font-size:x-small;
          }
          .story
          {
          background-color: lightGreen;
          padding: 6px 6px 6px 6px;
          }
          .failedStory
          {
          background-color: #ffbbbb;
          padding: 6px 6px 6px 6px;
          }
          .scenarios
          {
          padding-left: 12px;
          padding-right: 12px;
          padding-top: 6px;
          padding-bottom: 6px;
          border-top: solid 0px lightGreen;
          border-bottom: solid 2px lightGreen;
          border-left: solid 2px lightGreen;
          border-right: solid 2px lightGreen;
          }
          
          .failedScenarios
          {
          padding-left: 12px;
          padding-right: 12px;
          padding-top: 6px;
          padding-bottom: 6px;
          border-top: solid 0px #ffbbbb;
          border-bottom: solid 2px #ffbbbb;
          border-left: solid 2px #ffbbbb;
          border-right: solid 2px #ffbbbb;
          }
          
          .scenarioTitle{
            font-weight:bold;
            color:darkgreen;
          }
          
          .failedScenarioTitle{
            font-weight:bold;
            color:red;
          }
          ]]>
        </style>
        <script type="text/javascript">

          <![CDATA[
          function lowerThan(value, comparison){
            return value ]]><xsl:value-of select="'&lt;'" disable-output-escaping="yes"/><![CDATA[comparison;
          }

          function greaterThan(value, comparison){
            return value ]]><xsl:value-of select="'&gt;'" disable-output-escaping="yes"/><![CDATA[ comparison;
          }
          ]]>
          <![CDATA[
            document.isCollapsed = true;
            
            function getElementsByClass(node,searchClass,tag) {
                var classElements = new Array();
                var elements = node.getElementsByTagName(tag); // use "*" for all elements
                
                var pattern = new RegExp("\b" + searchClass + "\b");
                for (i = 0, j = 0; lowerThan(i,elements.length); i++) {
                  var className = elements[i].className;
                  
                  if (greaterThan(className.indexOf(searchClass), -1)) {
                    classElements[j] = elements[i];
                    j++;
                  }
                }
                return classElements;
            }
          
            function toggleAll(){
              var elements = getElementsByClass(document, 'scenarios', 'div');
              toggleElements(elements);
              elements = getElementsByClass(document, 'failedScenarios', 'div');
              toggleElements(elements);
              document.isCollapsed = !document.isCollapsed;
            }
            
            function toggleElements(elements){
              for (i=0; lowerThan(i, elements.length); i++){
                var element = elements[i];
                element.style.display = document.isCollapsed ? 'block' : 'none';
              }
            }
            
            function toggle(divId){
              div = document.getElementById(divId);
              if (div!=null){
                if (div.style.display != 'none' ){
                  div.style.display = 'none';
                }
                else {
                  div.style.display = 'block'; 
                }
              }
            }
          ]]>
        </script>
      </head>
      <body>
        <table border="0" cellspacing="0" cellpadding="0" width="100%">
          <xsl:apply-templates select="/report/header" />

          <tr>
            <td class="report" style="padding-top: 6px; padding-bottom: 6px; padding-left: 12px;
                padding-right: 12px;">
              <xsl:apply-templates select="/report/summary" />
              <br />
              <xsl:apply-templates select="/report/stories" />
            </td>
          </tr>
          <xsl:apply-templates select="/report/footer" />
        </table>
      </body>
    </html>
  </xsl:template>

  <xsl:template match="/report/stories">
    <table border="0" cellspacing="0" cellpadding="0" width="100%">
      <tr>
        <td style="padding: 3px 3px 3px 3px" class="storiesHeader">
          Stories [<a href="javascript:" onclick="toggleAll();">Collapse/Expand All</a>]
        </td>
      </tr>
      <tr>
        <tr>
          <td class="storiesBody">
            <xsl:apply-templates select="story" />
          </td>
        </tr>
      </tr>
    </table>
  </xsl:template>

  <xsl:template match="/report/stories/story">
    <div style="margin-top:6px;">
      <xsl:if test ="@isSuccessful='true'">
        <xsl:attribute name="class">story</xsl:attribute>
      </xsl:if>
      <xsl:if test ="@isSuccessful='false'">
        <xsl:attribute name="class">failedStory</xsl:attribute>
      </xsl:if>
      <b>
        Story <xsl:value-of select ="@index"/>: [<a href="javascript:">
          <xsl:attribute name="onclick">toggle('div_<xsl:value-of select = "@index" />');</xsl:attribute>Collapse/Expand
        </a>]
      </b>
      <br />
      <xsl:value-of select ="@identity"/>
      <br />
      <xsl:value-of select ="@asA"/>
      <br />
      <xsl:value-of select ="@iWant"/>
      <br />
      <xsl:value-of select ="@soThat"/>
    </div>
    <div style="width:100%">
      <xsl:if test ="@isSuccessful='true'">
        <xsl:attribute name="style">display:none;</xsl:attribute>
        <xsl:attribute name="class">scenarios</xsl:attribute>
      </xsl:if>
      <xsl:if test ="@isSuccessful='false'">
        <xsl:attribute name="style">display:block;</xsl:attribute>
        <xsl:attribute name="class">failedScenarios</xsl:attribute>
      </xsl:if>
      <xsl:attribute name="id">div_<xsl:value-of select = "@index" /></xsl:attribute>
      <xsl:apply-templates select="scenario" />
    </div>
  </xsl:template>

  <xsl:template match="/report/stories/story/scenario">
    <div style="padding-top:6px; width:100%;">
      <b>
        <xsl:if test ="@isSuccessful='true'">
          <xsl:attribute name="class">scenarioTitle</xsl:attribute>
        </xsl:if>
        <xsl:if test ="@isSuccessful='false'">
          <xsl:attribute name="class">failedScenarioTitle</xsl:attribute>
        </xsl:if>
        Scenario <xsl:value-of select ="@index"/>
      </b>: <xsl:value-of select ="@description"/><br />
      Narrative:<br />
      <table border="0" cellspacing="0" cellpadding="0" width="98%">
        <colgroup>
          <col />
          <col style="width: 200px;" />
        </colgroup>
        <xsl:apply-templates select="action" />
        <tr class="totalTime">
          <td class="condition">
            <b>Total Scenario Time:</b>&#160;
            <xsl:value-of select ="@totalTime"/>&#160;
            seconds
          </td>
          <td class="totalTimeFinishTime">
            [<xsl:value-of select ="@finishTime"/>]
          </td>
        </tr>
      </table>
    </div>
  </xsl:template>

  <xsl:template match="/report/stories/story/scenario/action">
    <tr>
      <xsl:attribute name="class"><xsl:value-of select="@oddOrEven"/></xsl:attribute>
      <td>
        <xsl:attribute name="class"><xsl:value-of select="@type"/></xsl:attribute>
        <xsl:if test ="@type='action' and @index>1">
          <b>
            and
          </b>
        </xsl:if>
        <xsl:if test ="@type='condition'">
          <b>
            <xsl:value-of select ="@description"/>
          </b>
        </xsl:if>
        <xsl:if test ="@type='action'">
            <xsl:if test ="@status='FAILED'">
                <b>
                    <font color="red">
                        <xsl:value-of select ="@description"/>
                    </font>
                </b>
            </xsl:if>
            <xsl:if test ="@status='SUCCESSFUL'">
                <b>
                    <xsl:value-of select ="@description"/>
                </b>
            </xsl:if>
            <xsl:if test ="@status='UNKNOWN'">
                <b>
                    <font color="#555555">
                        <xsl:value-of select ="@description"/>
                    </font>
                </b>
            </xsl:if>
        </xsl:if>
      </td>
      <td>
        <xsl:if test ="@type='action'">
          <xsl:attribute name="class">actionTime</xsl:attribute>
          [<xsl:value-of select ="@actionTime"/>]
        </xsl:if>
        <xsl:if test ="@type='condition'">
          &#160;
        </xsl:if>
      </td>
    </tr>
  </xsl:template>

  <xsl:template match="/report/summary">
    <table border="0" cellspacing="0" cellpadding="0" style="width: 33%">
      <tr>
        <td style="padding: 3px 3px 3px 3px">
          <xsl:if test="@failedScenarios>0">
            <span class="runFailed">Test run failed!</span>
          </xsl:if>
          <xsl:if test="@failedScenarios=0">
            <span class="runSucceeded">Test run succeeded!</span>
          </xsl:if>
        </td>
      </tr>
      <tr>
        <td class="summary" style="padding: 3px 3px 3px 3px">
          <b>Summary:</b><br />
          Total Stories: <xsl:value-of select ="@totalStories" /><br />
          Total Scenarios: <xsl:value-of select ="@totalScenarios" /><br />
          Scenarios Succeeded: <span class="successfulTests">
            <xsl:value-of select ="@successfulScenarios" /> (<xsl:value-of select ="@percentageSuccessful" />%)
          </span><br />
          Scenarios Failed: <span class="failedTests">
            <xsl:value-of select ="@failedScenarios" /> (<xsl:value-of select ="@percentageFailed" />%)
          </span><br />
        </td>
      </tr>
    </table>
  </xsl:template>

  <xsl:template match="/report/header">
    <tr>
      <td class="header">
        Pyccuracy - Tests Run Report -
        <span class="date">
          <xsl:value-of select ="@date"/>
        </span>
      </td>
    </tr>
  </xsl:template>
  <xsl:template match="/report/footer">
    <tr>
      <td class="footer">
        Pyccuracy - Version <xsl:value-of select ="@version"/> - <a href="http://www.pyccuracy.org">http://www.pyccuracy.org</a>
      </td>
    </tr>
  </xsl:template>
</xsl:stylesheet>
