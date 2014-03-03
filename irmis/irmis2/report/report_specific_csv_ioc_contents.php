<?php

 /*
  * Written by Dawn Clemons
  * Specialized step in creating a CSV report. Information that applies only
  * to the IOC PHP viewer is written in the same order as it appeared in the
  * viewer.
  */

   //The file pointer $fp was already declared in report_generic_csv.php

      //Get the data
	  $iocContentsList = $_SESSION['iocContentsList'];
	  $iocContentsEntities = $iocContentsList->getArray();
	  
      foreach ($iocContentsEntities as $iocContentsEntity) {
	  
      if ($iocContentsEntity->getLogicalDesc()=='0') {
	      $slot0 = $iocContentsEntity->getComponentTypeName();
	  }
      if ($iocContentsEntity->getLogicalDesc()=='1') {
	      $slot1 = $iocContentsEntity->getComponentTypeName();
	  }
	  if (($iocContentsEntity->getLogicalDesc()=='R1')||($iocContentsEntity->getLogicalDesc()=='1R')) {
	      $slot1r = $iocContentsEntity->getComponentTypeName();
	  }
	  if ($iocContentsEntity->getLogicalDesc()=='2') {
	      $slot2 = $iocContentsEntity->getComponentTypeName();
	  }
	  if (($iocContentsEntity->getLogicalDesc()=='R2')||($iocContentsEntity->getLogicalDesc()=='2R')) {
	      $slot2r = $iocContentsEntity->getComponentTypeName();
	  }
	  if ($iocContentsEntity->getLogicalDesc()=='3') {
	      $slot3 = $iocContentsEntity->getComponentTypeName();
	  }
	  if (($iocContentsEntity->getLogicalDesc()=='R3')||($iocContentsEntity->getLogicalDesc()=='3R')) {
	      $slot3r = $iocContentsEntity->getComponentTypeName();
	  }
	  if ($iocContentsEntity->getLogicalDesc()=='4') {
	      $slot4 = $iocContentsEntity->getComponentTypeName();
	  }
	  if (($iocContentsEntity->getLogicalDesc()=='R4')||($iocContentsEntity->getLogicalDesc()=='4R')) {
	      $slot4r = $iocContentsEntity->getComponentTypeName();
	  }
	  if ($iocContentsEntity->getLogicalDesc()=='5') {
	      $slot5 = $iocContentsEntity->getComponentTypeName();
	  }
	  if (($iocContentsEntity->getLogicalDesc()=='R5')||($iocContentsEntity->getLogicalDesc()=='5R')) {
	      $slot5r = $iocContentsEntity->getComponentTypeName();
	  }
	  if ($iocContentsEntity->getLogicalDesc()=='6') {
	      $slot6 = $iocContentsEntity->getComponentTypeName();
	  }
	  if (($iocContentsEntity->getLogicalDesc()=='R6')||($iocContentsEntity->getLogicalDesc()=='6R')) {
	      $slot6r = $iocContentsEntity->getComponentTypeName();
	  }
	  if ($iocContentsEntity->getLogicalDesc()=='7') {
	      $slot7 = $iocContentsEntity->getComponentTypeName();
	  }
	  if (($iocContentsEntity->getLogicalDesc()=='R7')||($iocContentsEntity->getLogicalDesc()=='7R')) {
	      $slot7r = $iocContentsEntity->getComponentTypeName();
	  }
	  if ($iocContentsEntity->getLogicalDesc()=='8') {
	      $slot8 = $iocContentsEntity->getComponentTypeName();
	  }
	  if (($iocContentsEntity->getLogicalDesc()=='R8')||($iocContentsEntity->getLogicalDesc()=='8R')) {
	      $slot8r = $iocContentsEntity->getComponentTypeName();
	  }
	  if ($iocContentsEntity->getLogicalDesc()=='9') {
	      $slot9 = $iocContentsEntity->getComponentTypeName();
	  }
	  if (($iocContentsEntity->getLogicalDesc()=='R9')||($iocContentsEntity->getLogicalDesc()=='9R')) {
	      $slot9r = $iocContentsEntity->getComponentTypeName();
	  }
	  if ($iocContentsEntity->getLogicalDesc()=='10') {
	      $slot10 = $iocContentsEntity->getComponentTypeName();
	  }
	  if (($iocContentsEntity->getLogicalDesc()=='R10')||($iocContentsEntity->getLogicalDesc()=='10R')) {
	      $slot10r = $iocContentsEntity->getComponentTypeName();
	  }
	  if ($iocContentsEntity->getLogicalDesc()=='11') {
	      $slot11 = $iocContentsEntity->getComponentTypeName();
	  }
	  if (($iocContentsEntity->getLogicalDesc()=='R11')||($iocContentsEntity->getLogicalDesc()=='11R')) {
	      $slot11r = $iocContentsEntity->getComponentTypeName();
	  }
	  if ($iocContentsEntity->getLogicalDesc()=='12') {
	      $slot12 = $iocContentsEntity->getComponentTypeName();
	  }
	  if (($iocContentsEntity->getLogicalDesc()=='R12')||($iocContentsEntity->getLogicalDesc()=='12R')) {
	      $slot12r = $iocContentsEntity->getComponentTypeName();
	  }
	  if ($iocContentsEntity->getLogicalDesc()=='13') {
	      $slot13 = $iocContentsEntity->getComponentTypeName();
	  }
	  if (($iocContentsEntity->getLogicalDesc()=='R13')||($iocContentsEntity->getLogicalDesc()=='13R')) {
	      $slot13r = $iocContentsEntity->getComponentTypeName();
	  }
	  if ($iocContentsEntity->getLogicalDesc()=='14') {
	      $slot14 = $iocContentsEntity->getComponentTypeName();
	  }
	  if (($iocContentsEntity->getLogicalDesc()=='R14')||($iocContentsEntity->getLogicalDesc()=='14R')) {
	      $slot14r = $iocContentsEntity->getComponentTypeName();
	  }
	  if ($iocContentsEntity->getLogicalDesc()=='15') {
	      $slot15 = $iocContentsEntity->getComponentTypeName();
	  }
	  if (($iocContentsEntity->getLogicalDesc()=='R15')||($iocContentsEntity->getLogicalDesc()=='15R')) {
	      $slot15r = $iocContentsEntity->getComponentTypeName();
	  }
	  if ($iocContentsEntity->getLogicalDesc()=='16') {
	      $slot16 = $iocContentsEntity->getComponentTypeName();
	  }
	  if (($iocContentsEntity->getLogicalDesc()=='R16')||($iocContentsEntity->getLogicalDesc()=='16R')) {
	      $slot16r = $iocContentsEntity->getComponentTypeName();
	  }
	  if ($iocContentsEntity->getLogicalDesc()=='17') {
	      $slot17 = $iocContentsEntity->getComponentTypeName();
	  }
	  if (($iocContentsEntity->getLogicalDesc()=='R17')||($iocContentsEntity->getLogicalDesc()=='17R')) {
	      $slot17r = $iocContentsEntity->getComponentTypeName();
	  }
	  if ($iocContentsEntity->getLogicalDesc()=='18') {
	      $slot18 = $iocContentsEntity->getComponentTypeName();
	  }
	  if (($iocContentsEntity->getLogicalDesc()=='R18')||($iocContentsEntity->getLogicalDesc()=='18R')) {
	      $slot18r = $iocContentsEntity->getComponentTypeName();
	  }
	  if ($iocContentsEntity->getLogicalDesc()=='19') {
	      $slot19 = $iocContentsEntity->getComponentTypeName();
	  }
	  if (($iocContentsEntity->getLogicalDesc()=='R19')||($iocContentsEntity->getLogicalDesc()=='19R')) {
	      $slot19r = $iocContentsEntity->getComponentTypeName();
	  }
	  if ($iocContentsEntity->getLogicalDesc()=='20') {
	      $slot20 = $iocContentsEntity->getComponentTypeName();
	  }
	  if (($iocContentsEntity->getLogicalDesc()=='R20')||($iocContentsEntity->getLogicalDesc()=='20R')) {
	      $slot20r = $iocContentsEntity->getComponentTypeName();
	  }
	  if ($iocContentsEntity->getLogicalDesc()=='21') {
	      $slot21 = $iocContentsEntity->getComponentTypeName();
	  }
	  if (($iocContentsEntity->getLogicalDesc()=='R21')||($iocContentsEntity->getLogicalDesc()=='21R')) {
	      $slot21r = $iocContentsEntity->getComponentTypeName();
	  }
	  }
	  
	  
	  $Embedded = "(Embedded IOC)";
	  $Softioc = "Soft IOC on Server";
	  if ($_SESSION['prevIF'] == Embedded) {
	    $clem = $Embedded;
	  } elseif ($_SESSION['prevIF'] == Soft_IOC) {
	    $clem = $Softioc;
	  }
	  $delim = ",";
	  fwrite ($fp, "\r\n");
	  
      fwrite ($fp, "\"".$_SESSION['prevCompName']."\"".$delim);
	  fwrite ($fp, "\"".$clem."\"".$delim."\"".$_SESSION['prevCompInstName']."\""."\r\n");
	  fwrite ($fp, "\"".$_SESSION['iocName']." (".$_SESSION['componentID'].")\""."\r\n\n");
	  
	  fwrite ($fp, "Front".$delim."Slot".$delim."Rear"."\r\n");
	  
	  if ($slot0) {
	  fwrite($fp, "\"".$slot0."\"".$delim); 
	  fwrite($fp, "\""."Slot 0"."\"".$delim);
	  fwrite($fp, "\"".$slot0r."\""."\r\n");	  
      }
	  
	  fwrite($fp, "\"".$slot1."\"".$delim); 
	  fwrite($fp, "\""."Slot 1"."\"".$delim);
	  fwrite($fp, "\"".$slot1r."\""."\r\n");

	  fwrite($fp, "\"".$slot2."\"".$delim);
	  fwrite($fp, "\""."Slot 2"."\"".$delim);
	  fwrite($fp, "\"".$slot2r."\""."\r\n");
	  
	  fwrite($fp, "\"".$slot3."\"".$delim);
	  fwrite($fp, "\""."Slot 3"."\"".$delim);
	  fwrite($fp, "\"".$slot3r."\""."\r\n");
	  
	  fwrite($fp, "\"".$slot4."\"".$delim);
	  fwrite($fp, "\""."Slot 4"."\"".$delim);
	  fwrite($fp, "\"".$slot4r."\""."\r\n");
	  
	  fwrite($fp, "\"".$slot5."\"".$delim);
	  fwrite($fp, "\""."Slot 5"."\"".$delim);
	  fwrite($fp, "\"".$slot5r."\""."\r\n");
	  
	  fwrite($fp, "\"".$slot6."\"".$delim);
	  fwrite($fp, "\""."Slot 6"."\"".$delim);
	  fwrite($fp, "\"".$slot6r."\""."\r\n");
	  
	  fwrite($fp, "\"".$slot7."\"".$delim);
	  fwrite($fp, "\""."Slot 7"."\"".$delim);
	  fwrite($fp, "\"".$slot7r."\""."\r\n");
	  
	  fwrite($fp, "\"".$slot8."\"".$delim);
	  fwrite($fp, "\""."Slot 8"."\"".$delim);
	  fwrite($fp, "\"".$slot8r."\""."\r\n");
	  
	  fwrite($fp, "\"".$slot9."\"".$delim);
	  fwrite($fp, "\""."Slot 9"."\"".$delim);
	  fwrite($fp, "\"".$slot9r."\""."\r\n");
	  
	  fwrite($fp, "\"".$slot10."\"".$delim);
	  fwrite($fp, "\""."Slot 10"."\"".$delim);
	  fwrite($fp, "\"".$slot10r."\""."\r\n");
	  
	  fwrite($fp, "\"".$slot11."\"".$delim);
	  fwrite($fp, "\""."Slot 11"."\"".$delim);
	  fwrite($fp, "\"".$slot11r."\""."\r\n");
	  
	  fwrite($fp, "\"".$slot12."\"".$delim);
	  fwrite($fp, "\""."Slot 12"."\"".$delim);
	  fwrite($fp, "\"".$slot12r."\""."\r\n");
	  
	  if (!$slot0) {
	  fwrite($fp, "\"".$slot13."\"".$delim);
	  fwrite($fp, "\""."Slot 13"."\"".$delim);
	  fwrite($fp, "\"".$slot13r."\""."\r\n");
	  
	  fwrite($fp, "\"".$slot14."\"".$delim);
	  fwrite($fp, "\""."Slot 14"."\"".$delim);
	  fwrite($fp, "\"".$slot14r."\""."\r\n");
	  
	  fwrite($fp, "\"".$slot15."\"".$delim);
	  fwrite($fp, "\""."Slot 15"."\"".$delim);
	  fwrite($fp, "\"".$slot15r."\""."\r\n");
	  
	  fwrite($fp, "\"".$slot16."\"".$delim);
	  fwrite($fp, "\""."Slot 16"."\"".$delim);
	  fwrite($fp, "\"".$slot16r."\""."\r\n");
	  
	  fwrite($fp, "\"".$slot17."\"".$delim);
	  fwrite($fp, "\""."Slot 17"."\"".$delim);
	  fwrite($fp, "\"".$slot17r."\""."\r\n");
	  
	  fwrite($fp, "\"".$slot18."\"".$delim);
	  fwrite($fp, "\""."Slot 18"."\"".$delim);
	  fwrite($fp, "\"".$slot18r."\""."\r\n");
	  
	  fwrite($fp, "\"".$slot19."\"".$delim);
	  fwrite($fp, "\""."Slot 19"."\"".$delim);
	  fwrite($fp, "\"".$slot19r."\""."\r\n");
	  
	  fwrite($fp, "\"".$slot20."\"".$delim);
	  fwrite($fp, "\""."Slot 20"."\"".$delim);
	  fwrite($fp, "\"".$slot20r."\""."\r\n");
	  
	  fwrite($fp, "\"".$slot21."\"".$delim);
	  fwrite($fp, "\""."Slot 21"."\"".$delim);
	  fwrite($fp, "\"".$slot21r."\""."\r\n");
      }

?>