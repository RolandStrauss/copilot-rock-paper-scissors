<mxfile host="app.diagrams.net">
  <diagram name="System Flow" id="system_flow">
    <!-- System Flow Diagram for Rock-Paper-Scissors-Lizard-Spock Game -->
    <mxGraphModel dx="1000" dy="1000" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <!-- Start -->
        <mxCell id="2" value="Start" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FF9800;strokeColor=#000000;" vertex="1" parent="1">
          <mxGeometry x="80" y="40" width="100" height="60" as="geometry" />
        </mxCell>
        <!-- Enter Names -->
        <mxCell id="3" value="Enter Player Name(s)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF176;strokeColor=#000000;" vertex="1" parent="1">
          <mxGeometry x="80" y="140" width="180" height="60" as="geometry" />
        </mxCell>
        <!-- Select Game Mode -->
        <mxCell id="4" value="Select Game Mode\n(Single/Two Player)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF176;strokeColor=#000000;" vertex="1" parent="1">
          <mxGeometry x="80" y="240" width="180" height="60" as="geometry" />
        </mxCell>
        <!-- Show Rules -->
        <mxCell id="5" value="Show Rules" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#B39DDB;strokeColor=#000000;" vertex="1" parent="1">
          <mxGeometry x="80" y="340" width="120" height="60" as="geometry" />
        </mxCell>
        <!-- Play Rounds -->
        <mxCell id="6" value="Play 3 Rounds\n(Select RPSLS)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#AED581;strokeColor=#000000;" vertex="1" parent="1">
          <mxGeometry x="80" y="440" width="180" height="60" as="geometry" />
        </mxCell>
        <!-- Score Tracking -->
        <mxCell id="7" value="Update & Display Scores" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#81D4FA;strokeColor=#000000;" vertex="1" parent="1">
          <mxGeometry x="80" y="540" width="180" height="60" as="geometry" />
        </mxCell>
        <!-- Sound Effects -->
        <mxCell id="8" value="Play Sound Effects" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFCCBC;strokeColor=#000000;" vertex="1" parent="1">
          <mxGeometry x="320" y="440" width="140" height="60" as="geometry" />
        </mxCell>
        <!-- Save High Scores -->
        <mxCell id="9" value="Save High Scores" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFD54F;strokeColor=#000000;" vertex="1" parent="1">
          <mxGeometry x="80" y="640" width="140" height="60" as="geometry" />
        </mxCell>
        <!-- Replay Option -->
        <mxCell id="10" value="Replay?" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FF9800;strokeColor=#000000;" vertex="1" parent="1">
          <mxGeometry x="80" y="740" width="100" height="60" as="geometry" />
        </mxCell>
        <!-- End -->
        <mxCell id="11" value="End" style="ellipse;whiteSpace=wrap;html=1;fillColor=#E57373;strokeColor=#000000;" vertex="1" parent="1">
          <mxGeometry x="80" y="840" width="100" height="60" as="geometry" />
        </mxCell>
        <!-- Connectors -->
        <mxCell id="12" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=1;" edge="1" parent="1" source="2" target="3">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="13" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=1;" edge="1" parent="1" source="3" target="4">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="14" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=1;" edge="1" parent="1" source="4" target="5">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="15" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=1;" edge="1" parent="1" source="5" target="6">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="16" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=1;" edge="1" parent="1" source="6" target="7">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="17" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=1;" edge="1" parent="1" source="7" target="9">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="18" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=1;" edge="1" parent="1" source="9" target="10">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="19" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=1;" edge="1" parent="1" source="10" target="11">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- Sound Effects from Play Rounds -->
        <mxCell id="20" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=1;dashed=1;" edge="1" parent="1" source="6" target="8">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
