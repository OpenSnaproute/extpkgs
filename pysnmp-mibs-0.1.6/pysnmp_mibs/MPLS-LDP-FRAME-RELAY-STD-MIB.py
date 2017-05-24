#
# PySNMP MIB module MPLS-LDP-FRAME-RELAY-STD-MIB (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/MPLS-LDP-FRAME-RELAY-STD-MIB
# Produced by pysmi-0.0.7 at Sun Feb 14 00:21:32 2016
# On host bldfarm platform Linux version 4.1.13-100.fc21.x86_64 by user goose
# Using Python version 3.5.0 (default, Jan  5 2016, 17:11:52) 
#
( Integer, OctetString, ObjectIdentifier, ) = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
( DLCI, ) = mibBuilder.importSymbols("FRAME-RELAY-DTE-MIB", "DLCI")
( InterfaceIndexOrZero, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
( mplsLdpEntityLdpId, mplsLdpEntityIndex, mplsLdpPeerLdpId, ) = mibBuilder.importSymbols("MPLS-LDP-STD-MIB", "mplsLdpEntityLdpId", "mplsLdpEntityIndex", "mplsLdpPeerLdpId")
( mplsStdMIB, ) = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "mplsStdMIB")
( NotificationGroup, ObjectGroup, ModuleCompliance, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
( Bits, ObjectIdentity, iso, MibIdentifier, ModuleIdentity, IpAddress, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, TimeTicks, Integer32, NotificationType, Counter64, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "iso", "MibIdentifier", "ModuleIdentity", "IpAddress", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "TimeTicks", "Integer32", "NotificationType", "Counter64")
( DisplayString, TextualConvention, RowStatus, StorageType, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus", "StorageType")
mplsLdpFrameRelayStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 166, 6)).setRevisions(("2004-06-03 00:00",))
if mibBuilder.loadTexts: mplsLdpFrameRelayStdMIB.setLastUpdated('200406030000Z')
if mibBuilder.loadTexts: mplsLdpFrameRelayStdMIB.setOrganization('Multiprotocol Label Switching (mpls)\n                  Working Group')
if mibBuilder.loadTexts: mplsLdpFrameRelayStdMIB.setContactInfo('Joan Cucchiara (jcucchiara@mindspring.com)\n         Marconi Communications, Inc.\n\n         Hans Sjostrand (hans@ipunplugged.com)\n         ipUnplugged\n\n         James V. Luciani (james_luciani@mindspring.com)\n         Marconi Communications, Inc.\n\n         Working Group Chairs:\n         George Swallow,   email: swallow@cisco.com\n         Loa Andersson,    email: loa@pi.se\n\n         MPLS Working Group, email: mpls@uu.net\n    ')
if mibBuilder.loadTexts: mplsLdpFrameRelayStdMIB.setDescription('Copyright (C) The Internet Society (year). The\n        initial version of this MIB module was published\n        in RFC 3815. For full legal notices see the RFC\n        itself or see:\n        http://www.ietf.org/copyrights/ianamib.html\n\n        This MIB contains managed object definitions for\n        configuring and monitoring the Multiprotocol Label\n        Switching (MPLS), Label Distribution Protocol (LDP),\n        utilizing Frame Relay as the Layer 2 media.')
mplsLdpFrameRelayObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 6, 1))
mplsLdpFrameRelayConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 6, 2))
mplsLdpEntityFrameRelayObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1))
mplsLdpEntityFrameRelayTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 1), )
if mibBuilder.loadTexts: mplsLdpEntityFrameRelayTable.setDescription("This table contains Frame Relay specific\n        information which could be used in the\n        'Optional Parameters' and other Frame Relay\n        specific information.\n\n        This table 'sparse augments' the mplsLdpEntityTable\n        when Frame Relay is the Layer 2 medium.")
mplsLdpEntityFrameRelayEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 1, 1), ).setIndexNames((0, "MPLS-LDP-STD-MIB", "mplsLdpEntityLdpId"), (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityIndex"))
if mibBuilder.loadTexts: mplsLdpEntityFrameRelayEntry.setDescription('An entry in this table represents the Frame Relay\n        optional parameters associated with the LDP entity.')
mplsLdpEntityFrameRelayIfIndexOrZero = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 1, 1, 1), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLdpEntityFrameRelayIfIndexOrZero.setDescription("This value represents either the InterfaceIndex of\n       the 'ifLayer' where the Frame Relay Labels 'owned' by this\n       entry were created, or 0 (zero).  The value of zero\n       means that the InterfaceIndex is not known.  For example,\n       if the InterfaceIndex is created subsequent to the\n       Frame Relay Label's creation, then it would not be known.\n       However, if the InterfaceIndex is known, then it must\n       be represented by this value.\n\n       If an InterfaceIndex becomes known, then the\n       network management entity (e.g., SNMP agent) responsible\n       for this object MUST change the value from 0 (zero) to the\n       value of the InterfaceIndex.  If an Frame Relay Label is\n       being used in forwarding data, then the value of this\n       object MUST be the InterfaceIndex.")
mplsLdpEntityFrameRelayMergeCap = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1,))).clone(namedValues=NamedValues(("notSupported", 0), ("supported", 1),))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLdpEntityFrameRelayMergeCap.setDescription("This represents whether or not the Frame Relay merge\n        capability is supported.  This is the EXACT value for the\n        Frame Relay Session Parameter, field M (for Frame Relay\n        Merge Capabilities).  The Frame Relay Session Parameter\n        is an optional parameter in the Initialization Message.\n\n\n        The description from rfc3036.txt is:\n        'M, Frame Relay Merge Capabilities\n           Specifies the merge capabilities of a Frame\n           Relay switch.  The following values are\n           supported in this version of the\n           specification:\n\n                  Value          Meaning\n\n                    0            Merge not supported\n                    1            Merge supported\n\n           Non-merge and merge Frame Relay LSRs may\n           freely interoperate.'\n\n           Please refer to the following reference for a\n           complete description of this feature.")
mplsLdpEntityFrameRelayLRComponents = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1,65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLdpEntityFrameRelayLRComponents.setDescription("Number of Label Range Components in the Initialization\n        message.  This also represents the number of entries\n        in the mplsLdpEntityFrameRelayLRTable which correspond\n        to this entry.\n\n        This is the EXACT value for the Frame Relay Session\n        Parameter, field N (for Number of label range\n        components).  The Frame Relay Session Parameter\n        is an optional parameter in the Initialization\n        Message.\n\n        The description from rfc3036.txt is:\n\n        'N, Number of label range components\n            Specifies the number of Frame Relay Label\n            Range Components included in the TLV.'\n\n         Please refer to the following reference for a\n         complete description of this feature.")
mplsLdpEntityFrameRelayVcDirectionality = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1,))).clone(namedValues=NamedValues(("bidirectional", 0), ("unidirection", 1),))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLdpEntityFrameRelayVcDirectionality.setDescription("If the value of this object is 'bidirectional(0)', then\n        the LSR supports the use of a given DLCI as a label for\n        both directions independently.  If the value of\n        this object is 'unidirectional(1)', then the LSR\n        uses the given DLCI as a label in only one direction.\n\n        This is the EXACT value for the Frame Relay Session\n        Parameter, field D (for VC Directionality).  The\n        Frame Relay Session Parameter is an optional\n        parameter in the Initialization Message.\n\n        The description from rfc3036.txt is:\n\n        'D, VC Directionality\n           A value of 0 specifies bidirectional VC capability,\n           meaning the LSR can support the use of a given\n           DLCI as a label for both link directions\n           independently.  A value of 1 specifies\n           unidirectional VC capability, meaning a given\n           DLCI may appear in a label mapping for one\n           direction on the link only.  When either or both\n           of the peers specifies unidirectional VC\n           capability, both LSRs use unidirectional VC\n           label assignment for the link as follows.  The\n           LSRs compare their LDP Identifiers as unsigned\n           integers.  The LSR with the larger LDP\n           Identifier may assign only odd-numbered DLCIs\n           in the range as labels.  The system with the\n           smaller LDP Identifier may assign only\n           even-numbered DLCIs in the range as labels.'\n\n           Please refer to the following reference for a\n           complete description of this feature.")
mplsLdpEntityFrameRelayStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 1, 1, 5), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLdpEntityFrameRelayStorageType.setDescription("The storage type for this conceptual row.\n        Conceptual rows having the value 'permanent(4)'\n        need not allow write-access to any columnar\n        objects in the row.")
mplsLdpEntityFrameRelayRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLdpEntityFrameRelayRowStatus.setDescription("The status of this conceptual row.  All writable\n         objects in this row may be modified at any time,\n         however, as described in detail in the section\n         entitled, 'Changing Values After Session\n         Establishment', and again described in the\n         DESCRIPTION clause of the\n         mplsLdpEntityAdminStatus object,\n         if a session has been initiated with a Peer,\n         changing objects in this table will\n         wreak havoc with the session and interrupt\n         traffic.  To repeat again:\n         the recommended procedure is to set the\n         mplsLdpEntityAdminStatus to\n         down, thereby explicitly causing a\n         session to be torn down. Then,\n         change objects in this entry, then set\n         the mplsLdpEntityAdminStatus\n         to enable which enables a new session\n         to be initiated.")
mplsLdpEntityFrameRelayLRTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 2), )
if mibBuilder.loadTexts: mplsLdpEntityFrameRelayLRTable.setDescription("This table contains information about the\n\n        Optional Parameters for the Frame Relay Session\n        in the LDP Initialization Message, specifically\n        it contains information about the Frame Relay\n        Label Range Components.\n\n        If the value of the object\n        'mplsLdpEntityOptionalParameters' contains the\n        value of 'frameRelaySessionParameters(3)' then\n        there must be at least one corresponding entry\n        in this table.")
mplsLdpEntityFrameRelayLREntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 2, 1), ).setIndexNames((0, "MPLS-LDP-STD-MIB", "mplsLdpEntityLdpId"), (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityIndex"), (0, "MPLS-LDP-FRAME-RELAY-STD-MIB", "mplsLdpEntityFrameRelayLRMinDlci"))
if mibBuilder.loadTexts: mplsLdpEntityFrameRelayLREntry.setDescription('An entry in this table represents the Frame Relay\n        Label Range Component associated with the LDP entity.')
mplsLdpEntityFrameRelayLRMinDlci = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 2, 1, 1), DLCI())
if mibBuilder.loadTexts: mplsLdpEntityFrameRelayLRMinDlci.setDescription("The lower bound which is supported.  This value\n        should be the same as that in the Frame Relay Label\n        Range Component's Minimum DLCI field.  The value\n        of zero is valid for the minimum DLCI field of\n        the label.")
mplsLdpEntityFrameRelayLRMaxDlci = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 2, 1, 2), DLCI()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLdpEntityFrameRelayLRMaxDlci.setDescription("The upper bound which is supported.  This value\n        should be the same as that in the Frame Relay Label\n        Range Component's Maximum DLCI field.")
mplsLdpEntityFrameRelayLRLen = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2,))).clone(namedValues=NamedValues(("tenDlciBits", 0), ("twentyThreeDlciBits", 2),))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLdpEntityFrameRelayLRLen.setDescription("This object specifies the length of the DLCI bits.\n\n        This is the EXACT value for the Len field of the\n        Frame Relay Label Range Component.\n\n        The description from rfc3036.txt is:\n\n        'Len\n            This field specifies the number of bits of the DLCI.\n            The following values are supported:\n\n                 Len    DLCI bits\n\n                 0       10\n                 2       23\n\n            Len values 1 and 3 are reserved.'\n\n         Please refer to the following reference for a complete\n         description of this feature.")
mplsLdpEntityFrameRelayLRStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 2, 1, 4), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLdpEntityFrameRelayLRStorageType.setDescription("The storage type for this conceptual row.\n        Conceptual rows having the value 'permanent(4)'\n        need not allow write-access to any columnar\n        objects in the row.")
mplsLdpEntityFrameRelayLRRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLdpEntityFrameRelayLRRowStatus.setDescription("The status of this conceptual row.  All writable\n         objects in this row may be modified at any time,\n         however, as described in detail in the section\n         entitled, 'Changing Values After Session\n         Establishment', and again described in the\n         DESCRIPTION clause of the\n         mplsLdpEntityAdminStatus object,\n         if a session has been initiated with a Peer,\n         changing objects in this table will\n         wreak havoc with the session and interrupt\n         traffic.  To repeat again:\n         the recommended procedure is to set the\n         mplsLdpEntityAdminStatus to down, thereby\n         explicitly causing a session to be torn down. Then,\n         change objects in this entry, then set the\n         mplsLdpEntityAdminStatus to enable which enables\n         a new session to be initiated.")
mplsLdpFrameRelaySessionObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 2))
mplsLdpFrameRelaySessionTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 2, 1), )
if mibBuilder.loadTexts: mplsLdpFrameRelaySessionTable.setDescription("A table of Frame Relay label range intersections\n        between the LDP Entities and LDP Peers.\n        Each row represents a single label range intersection.\n\n        NOTE:  this table cannot use the 'AUGMENTS'\n\n        clause because there is not necessarily a one-to-one\n        mapping between this table and the\n        mplsLdpSessionTable.")
mplsLdpFrameRelaySessionEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 2, 1, 1), ).setIndexNames((0, "MPLS-LDP-STD-MIB", "mplsLdpEntityLdpId"), (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityIndex"), (0, "MPLS-LDP-STD-MIB", "mplsLdpPeerLdpId"), (0, "MPLS-LDP-FRAME-RELAY-STD-MIB", "mplsLdpFrameRelaySessionMinDlci"))
if mibBuilder.loadTexts: mplsLdpFrameRelaySessionEntry.setDescription('An entry in this table represents information on a\n        single label range intersection between an\n        LDP Entity and LDP Peer.\n\n        The information contained in a row is read-only.')
mplsLdpFrameRelaySessionMinDlci = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 2, 1, 1, 1), DLCI())
if mibBuilder.loadTexts: mplsLdpFrameRelaySessionMinDlci.setDescription('The lower bound of DLCIs which are supported.\n        The value of zero is a valid value for the\n        minimum DLCI field of the label.')
mplsLdpFrameRelaySessionMaxDlci = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 2, 1, 1, 2), DLCI()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLdpFrameRelaySessionMaxDlci.setDescription('The upper bound of DLCIs which are supported.')
mplsLdpFrameRelaySessionLen = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2,))).clone(namedValues=NamedValues(("tenDlciBits", 0), ("twentyThreeDlciBits", 2),))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLdpFrameRelaySessionLen.setDescription('This object specifies the DLCI bits.')
mplsLdpFrameRelayGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 6, 2, 1))
mplsLdpFrameRelayCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 6, 2, 2))
mplsLdpFrameRelayModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 166, 6, 2, 2, 1)).setObjects(*(("MPLS-LDP-FRAME-RELAY-STD-MIB", "mplsLdpFrameRelayGroup"),))
if mibBuilder.loadTexts: mplsLdpFrameRelayModuleFullCompliance.setDescription('The Module is implemented with support for\n        read-create and read-write.  In other words,\n        both monitoring and configuration\n        are available when using this MODULE-COMPLIANCE.')
mplsLdpFrameRelayModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 166, 6, 2, 2, 2)).setObjects(*(("MPLS-LDP-FRAME-RELAY-STD-MIB", "mplsLdpFrameRelayGroup"),))
if mibBuilder.loadTexts: mplsLdpFrameRelayModuleReadOnlyCompliance.setDescription('The Module is implemented with support for\n        read-only.  In other words, only monitoring\n        is available by implementing this MODULE-COMPLIANCE.')
mplsLdpFrameRelayGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 6, 2, 1, 1)).setObjects(*(("MPLS-LDP-FRAME-RELAY-STD-MIB", "mplsLdpEntityFrameRelayIfIndexOrZero"), ("MPLS-LDP-FRAME-RELAY-STD-MIB", "mplsLdpEntityFrameRelayMergeCap"), ("MPLS-LDP-FRAME-RELAY-STD-MIB", "mplsLdpEntityFrameRelayLRComponents"), ("MPLS-LDP-FRAME-RELAY-STD-MIB", "mplsLdpEntityFrameRelayVcDirectionality"), ("MPLS-LDP-FRAME-RELAY-STD-MIB", "mplsLdpEntityFrameRelayStorageType"), ("MPLS-LDP-FRAME-RELAY-STD-MIB", "mplsLdpEntityFrameRelayRowStatus"), ("MPLS-LDP-FRAME-RELAY-STD-MIB", "mplsLdpEntityFrameRelayLRMaxDlci"), ("MPLS-LDP-FRAME-RELAY-STD-MIB", "mplsLdpEntityFrameRelayLRLen"), ("MPLS-LDP-FRAME-RELAY-STD-MIB", "mplsLdpEntityFrameRelayLRStorageType"), ("MPLS-LDP-FRAME-RELAY-STD-MIB", "mplsLdpEntityFrameRelayLRRowStatus"), ("MPLS-LDP-FRAME-RELAY-STD-MIB", "mplsLdpFrameRelaySessionMaxDlci"), ("MPLS-LDP-FRAME-RELAY-STD-MIB", "mplsLdpFrameRelaySessionLen"),))
if mibBuilder.loadTexts: mplsLdpFrameRelayGroup.setDescription('Objects that apply to all MPLS LDP implementations\n        using Frame Relay as the Layer 2.')
mibBuilder.exportSymbols("MPLS-LDP-FRAME-RELAY-STD-MIB", mplsLdpEntityFrameRelayIfIndexOrZero=mplsLdpEntityFrameRelayIfIndexOrZero, PYSNMP_MODULE_ID=mplsLdpFrameRelayStdMIB, mplsLdpEntityFrameRelayStorageType=mplsLdpEntityFrameRelayStorageType, mplsLdpFrameRelayStdMIB=mplsLdpFrameRelayStdMIB, mplsLdpEntityFrameRelayLRComponents=mplsLdpEntityFrameRelayLRComponents, mplsLdpEntityFrameRelayLRRowStatus=mplsLdpEntityFrameRelayLRRowStatus, mplsLdpFrameRelaySessionLen=mplsLdpFrameRelaySessionLen, mplsLdpEntityFrameRelayLREntry=mplsLdpEntityFrameRelayLREntry, mplsLdpEntityFrameRelayVcDirectionality=mplsLdpEntityFrameRelayVcDirectionality, mplsLdpEntityFrameRelayRowStatus=mplsLdpEntityFrameRelayRowStatus, mplsLdpFrameRelaySessionEntry=mplsLdpFrameRelaySessionEntry, mplsLdpEntityFrameRelayLRTable=mplsLdpEntityFrameRelayLRTable, mplsLdpFrameRelayObjects=mplsLdpFrameRelayObjects, mplsLdpFrameRelayGroups=mplsLdpFrameRelayGroups, mplsLdpEntityFrameRelayLRMinDlci=mplsLdpEntityFrameRelayLRMinDlci, mplsLdpFrameRelayCompliances=mplsLdpFrameRelayCompliances, mplsLdpFrameRelayModuleFullCompliance=mplsLdpFrameRelayModuleFullCompliance, mplsLdpFrameRelaySessionTable=mplsLdpFrameRelaySessionTable, mplsLdpEntityFrameRelayObjects=mplsLdpEntityFrameRelayObjects, mplsLdpFrameRelayGroup=mplsLdpFrameRelayGroup, mplsLdpEntityFrameRelayLRStorageType=mplsLdpEntityFrameRelayLRStorageType, mplsLdpFrameRelaySessionMaxDlci=mplsLdpFrameRelaySessionMaxDlci, mplsLdpEntityFrameRelayEntry=mplsLdpEntityFrameRelayEntry, mplsLdpFrameRelayModuleReadOnlyCompliance=mplsLdpFrameRelayModuleReadOnlyCompliance, mplsLdpFrameRelaySessionMinDlci=mplsLdpFrameRelaySessionMinDlci, mplsLdpEntityFrameRelayMergeCap=mplsLdpEntityFrameRelayMergeCap, mplsLdpEntityFrameRelayLRLen=mplsLdpEntityFrameRelayLRLen, mplsLdpEntityFrameRelayLRMaxDlci=mplsLdpEntityFrameRelayLRMaxDlci, mplsLdpFrameRelaySessionObjects=mplsLdpFrameRelaySessionObjects, mplsLdpFrameRelayConformance=mplsLdpFrameRelayConformance, mplsLdpEntityFrameRelayTable=mplsLdpEntityFrameRelayTable)
