<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <!-- extra xsl:templates go here -->
    <xsl:strip-space elements="*" />
    <xsl:preserve-space elements="pre" />

    <xsl:template match="pre/text()" xmlns:str="http://exslt.org/strings" mode="initial-stage">
        <xsl:value-of select="str:replace(., '&#13;', '')"/>
    </xsl:template>

</xsl:stylesheet>
