#
# PySNMP MIB module IPS-AUTH-MIB (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/IPS-AUTH-MIB
# Produced by pysmi-0.0.7 at Sun Feb 14 00:18:17 2016
# On host bldfarm platform Linux version 4.1.13-100.fc21.x86_64 by user goose
# Using Python version 3.5.0 (default, Jan  5 2016, 17:11:52) 
#
( Integer, OctetString, ObjectIdentifier, ) = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
( AddressFamilyNumbers, ) = mibBuilder.importSymbols("IANA-ADDRESS-FAMILY-NUMBERS-MIB", "AddressFamilyNumbers")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( NotificationGroup, ObjectGroup, ModuleCompliance, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
( IpAddress, NotificationType, iso, Counter32, Integer32, mib_2, Gauge32, ModuleIdentity, Unsigned32, TimeTicks, MibIdentifier, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ) = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "NotificationType", "iso", "Counter32", "Integer32", "mib-2", "Gauge32", "ModuleIdentity", "Unsigned32", "TimeTicks", "MibIdentifier", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits")
( AutonomousType, TextualConvention, StorageType, DisplayString, RowStatus, ) = mibBuilder.importSymbols("SNMPv2-TC", "AutonomousType", "TextualConvention", "StorageType", "DisplayString", "RowStatus")
ipsAuthMibModule = ModuleIdentity((1, 3, 6, 1, 2, 1, 141)).setRevisions(("2006-05-22 00:00",))
if mibBuilder.loadTexts: ipsAuthMibModule.setLastUpdated('200605220000Z')
if mibBuilder.loadTexts: ipsAuthMibModule.setOrganization('IETF IPS Working Group')
if mibBuilder.loadTexts: ipsAuthMibModule.setContactInfo('\n    Mark Bakke\n    Postal: Cisco Systems, Inc\n    7900 International Drive, Suite 400\n    Bloomington, MN\n    USA 55425\n\n    E-mail: mbakke@cisco.com\n\n    James Muchow\n    Postal: Qlogic Corp.\n    6321 Bury Dr.\n    Eden Prairie, MN\n    USA 55346\n\n    E-Mail: james.muchow@qlogic.com')
if mibBuilder.loadTexts: ipsAuthMibModule.setDescription('The IP Storage Authorization MIB module.\n         Copyright (C) The Internet Society (2006).  This version of\n         this MIB module is part of RFC 4545;  see the RFC itself for\n         full legal notices.')
ipsAuthNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 141, 0))
ipsAuthObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 141, 1))
ipsAuthConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 141, 2))
class IpsAuthAddress(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,255)

ipsAuthDescriptors = MibIdentifier((1, 3, 6, 1, 2, 1, 141, 1, 1))
ipsAuthMethodTypes = ObjectIdentity((1, 3, 6, 1, 2, 1, 141, 1, 1, 1))
if mibBuilder.loadTexts: ipsAuthMethodTypes.setDescription('Registration point for Authentication Method Types.')
ipsAuthMethodNone = ObjectIdentity((1, 3, 6, 1, 2, 1, 141, 1, 1, 1, 1))
if mibBuilder.loadTexts: ipsAuthMethodNone.setDescription('The authoritative identifier when no authentication\n        method is used.')
ipsAuthMethodSrp = ObjectIdentity((1, 3, 6, 1, 2, 1, 141, 1, 1, 1, 2))
if mibBuilder.loadTexts: ipsAuthMethodSrp.setDescription('The authoritative identifier when the authentication\n        method is SRP.')
ipsAuthMethodChap = ObjectIdentity((1, 3, 6, 1, 2, 1, 141, 1, 1, 1, 3))
if mibBuilder.loadTexts: ipsAuthMethodChap.setDescription('The authoritative identifier when the authentication\n        method is CHAP.')
ipsAuthMethodKerberos = ObjectIdentity((1, 3, 6, 1, 2, 1, 141, 1, 1, 1, 4))
if mibBuilder.loadTexts: ipsAuthMethodKerberos.setDescription('The authoritative identifier when the authentication\n        method is Kerberos.')
ipsAuthInstance = MibIdentifier((1, 3, 6, 1, 2, 1, 141, 1, 2))
ipsAuthInstanceAttributesTable = MibTable((1, 3, 6, 1, 2, 1, 141, 1, 2, 2), )
if mibBuilder.loadTexts: ipsAuthInstanceAttributesTable.setDescription('A list of Authorization instances present on the system.')
ipsAuthInstanceAttributesEntry = MibTableRow((1, 3, 6, 1, 2, 1, 141, 1, 2, 2, 1), ).setIndexNames((0, "IPS-AUTH-MIB", "ipsAuthInstIndex"))
if mibBuilder.loadTexts: ipsAuthInstanceAttributesEntry.setDescription('An entry (row) containing management information\n        applicable to a particular Authorization instance.')
ipsAuthInstIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 2, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1,4294967295)))
if mibBuilder.loadTexts: ipsAuthInstIndex.setDescription('An arbitrary integer used to uniquely identify a\n        particular authorization instance.  This index value\n        must not be modified or reused by an agent unless\n        a reboot has occurred.  An agent should attempt to\n        keep this value persistent across reboots.')
ipsAuthInstDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 2, 2, 1, 2), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipsAuthInstDescr.setDescription('A character string, determined by the implementation to\n        describe the authorization instance.  When only a single\n        instance is present, this object may be set to the\n        zero-length string; with multiple authorization\n        instances, it must be set to a unique value in an\n        implementation-dependent manner to describe the purpose\n        of the respective instance.  If this is deployed in a\n        master agent with more than one subagent implementing\n        this MIB module, the master agent is responsible for\n        ensuring that this object is unique across all\n        subagents.')
ipsAuthInstStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 2, 2, 1, 3), StorageType().clone('volatile')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipsAuthInstStorageType.setDescription("The storage type for all read-write objects within this\n         row.  Rows in this table are always created via an\n         external process, and may have a storage type of readOnly\n         or permanent.  Conceptual rows having the value 'permanent'\n         need not allow write access to any columnar objects in\n         the row.\n\n         If this object has the value 'volatile', modifications\n         to read-write objects in this row are not persistent\n         across reboots.  If this object has the value\n         'nonVolatile', modifications to objects in this row\n         are persistent.\n\n         An implementation may choose to allow this object\n         to be set to either 'nonVolatile' or 'volatile',\n         allowing the management application to choose this\n         behavior.")
ipsAuthIdentity = MibIdentifier((1, 3, 6, 1, 2, 1, 141, 1, 3))
ipsAuthIdentAttributesTable = MibTable((1, 3, 6, 1, 2, 1, 141, 1, 3, 1), )
if mibBuilder.loadTexts: ipsAuthIdentAttributesTable.setDescription('A list of user identities, each belonging to a\n        particular ipsAuthInstance.')
ipsAuthIdentAttributesEntry = MibTableRow((1, 3, 6, 1, 2, 1, 141, 1, 3, 1, 1), ).setIndexNames((0, "IPS-AUTH-MIB", "ipsAuthInstIndex"), (0, "IPS-AUTH-MIB", "ipsAuthIdentIndex"))
if mibBuilder.loadTexts: ipsAuthIdentAttributesEntry.setDescription('An entry (row) containing management information\n        describing a user identity within an authorization\n        instance on this node.')
ipsAuthIdentIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 3, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1,4294967295)))
if mibBuilder.loadTexts: ipsAuthIdentIndex.setDescription('An arbitrary integer used to uniquely identify a\n        particular identity instance within an authorization\n        instance present on the node.  This index value\n        must not be modified or reused by an agent unless\n        a reboot has occurred.  An agent should attempt to\n        keep this value persistent across reboots.')
ipsAuthIdentDescription = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 3, 1, 1, 2), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthIdentDescription.setDescription('A character string describing this particular identity.')
ipsAuthIdentRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 3, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthIdentRowStatus.setDescription("This field allows entries to be dynamically added and\n        removed from this table via SNMP.  When adding a row to\n        this table, all non-Index/RowStatus objects must be set.\n        Rows may be discarded using RowStatus.  The value of\n        ipsAuthIdentDescription may be set while\n        ipsAuthIdentRowStatus is 'active'.")
ipsAuthIdentStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 3, 1, 1, 4), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthIdentStorageType.setDescription("The storage type for all read-create objects in this row.\n         Rows in this table that were created through an external\n         process may have a storage type of readOnly or permanent.\n         Conceptual rows having the value 'permanent' need not\n         allow write access to any columnar objects in the row.")
ipsAuthIdentityName = MibIdentifier((1, 3, 6, 1, 2, 1, 141, 1, 4))
ipsAuthIdentNameAttributesTable = MibTable((1, 3, 6, 1, 2, 1, 141, 1, 4, 1), )
if mibBuilder.loadTexts: ipsAuthIdentNameAttributesTable.setDescription('A list of unique names that can be used to positively\n        identify a particular user identity.')
ipsAuthIdentNameAttributesEntry = MibTableRow((1, 3, 6, 1, 2, 1, 141, 1, 4, 1, 1), ).setIndexNames((0, "IPS-AUTH-MIB", "ipsAuthInstIndex"), (0, "IPS-AUTH-MIB", "ipsAuthIdentIndex"), (0, "IPS-AUTH-MIB", "ipsAuthIdentNameIndex"))
if mibBuilder.loadTexts: ipsAuthIdentNameAttributesEntry.setDescription('An entry (row) containing management information\n        applicable to a unique identity name, which can be used\n        to identify a user identity within a particular\n        authorization instance.')
ipsAuthIdentNameIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 4, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1,4294967295)))
if mibBuilder.loadTexts: ipsAuthIdentNameIndex.setDescription('An arbitrary integer used to uniquely identify a\n        particular identity name instance within an\n        ipsAuthIdentity within an authorization instance.\n        This index value must not be modified or reused by\n        an agent unless a reboot has occurred.  An agent\n        should attempt to keep this value persistent across\n        reboots.')
ipsAuthIdentName = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 4, 1, 1, 2), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthIdentName.setDescription('A character string that is the unique name of an\n        identity that may be used to identify this ipsAuthIdent\n        entry.')
ipsAuthIdentNameRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 4, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthIdentNameRowStatus.setDescription("This field allows entries to be dynamically added and\n        removed from this table via SNMP.  When adding a row to\n        this table, all non-Index/RowStatus objects must be set.\n        Rows may be discarded using RowStatus.  The value of\n        ipsAuthIdentName may be set when this value is 'active'.")
ipsAuthIdentNameStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 4, 1, 1, 4), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthIdentNameStorageType.setDescription("The storage type for all read-create objects in this row.\n         Rows in this table that were created through an external\n         process may have a storage type of readOnly or permanent.\n         Conceptual rows having the value 'permanent' need not\n         allow write access to any columnar objects in the row.")
ipsAuthIdentityAddress = MibIdentifier((1, 3, 6, 1, 2, 1, 141, 1, 5))
ipsAuthIdentAddrAttributesTable = MibTable((1, 3, 6, 1, 2, 1, 141, 1, 5, 1), )
if mibBuilder.loadTexts: ipsAuthIdentAddrAttributesTable.setDescription('A list of address ranges that are allowed to serve\n        as the endpoint addresses of a particular identity.\n        An address range includes a starting and ending address\n        and an optional netmask, and an address type indicator,\n        which can specify whether the address is IPv4, IPv6,\n        FC-WWPN, or FC-WWNN.')
ipsAuthIdentAddrAttributesEntry = MibTableRow((1, 3, 6, 1, 2, 1, 141, 1, 5, 1, 1), ).setIndexNames((0, "IPS-AUTH-MIB", "ipsAuthInstIndex"), (0, "IPS-AUTH-MIB", "ipsAuthIdentIndex"), (0, "IPS-AUTH-MIB", "ipsAuthIdentAddrIndex"))
if mibBuilder.loadTexts: ipsAuthIdentAddrAttributesEntry.setDescription('An entry (row) containing management information\n        applicable to an address range that is used as part\n        of the authorization of an identity\n        within an authorization instance on this node.')
ipsAuthIdentAddrIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 5, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1,4294967295)))
if mibBuilder.loadTexts: ipsAuthIdentAddrIndex.setDescription('An arbitrary integer used to uniquely identify a\n        particular ipsAuthIdentAddress instance within an\n        ipsAuthIdentity within an authorization instance\n        present on the node.\n        This index value must not be modified or reused by\n        an agent unless a reboot has occurred.  An agent\n        should attempt to keep this value persistent across\n        reboots.')
ipsAuthIdentAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 5, 1, 1, 2), AddressFamilyNumbers()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthIdentAddrType.setDescription('The address types used in the ipsAuthIdentAddrStart\n        and ipsAuthAddrEnd objects.  This type is taken\n        from the IANA address family types.')
ipsAuthIdentAddrStart = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 5, 1, 1, 3), IpsAuthAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthIdentAddrStart.setDescription('The starting address of the allowed address range.\n        The format of this object is determined by\n        ipsAuthIdentAddrType.')
ipsAuthIdentAddrEnd = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 5, 1, 1, 4), IpsAuthAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthIdentAddrEnd.setDescription('The ending address of the allowed address range.\n        If the ipsAuthIdentAddrEntry specifies a single\n        address, this shall match the ipsAuthIdentAddrStart.\n        The format of this object is determined by\n        ipsAuthIdentAddrType.')
ipsAuthIdentAddrRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 5, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthIdentAddrRowStatus.setDescription("This field allows entries to be dynamically added and\n        removed from this table via SNMP.  When adding a row to\n        this table, all non-Index/RowStatus objects must be set.\n        Rows may be discarded using RowStatus.  The values of\n        ipsAuthIdentAddrStart and ipsAuthIdentAddrEnd may be set\n        when this value is 'active'.  The value of\n        ipsAuthIdentAddrType may not be set when this value is\n        'active'.")
ipsAuthIdentAddrStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 5, 1, 1, 6), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthIdentAddrStorageType.setDescription("The storage type for all read-create objects in this row.\n         Rows in this table that were created through an external\n         process may have a storage type of readOnly or permanent.\n         Conceptual rows having the value 'permanent' need not\n         allow write access to any columnar objects in the row.")
ipsAuthCredential = MibIdentifier((1, 3, 6, 1, 2, 1, 141, 1, 6))
ipsAuthCredentialAttributesTable = MibTable((1, 3, 6, 1, 2, 1, 141, 1, 6, 1), )
if mibBuilder.loadTexts: ipsAuthCredentialAttributesTable.setDescription('A list of credentials related to user identities\n        that are allowed as valid authenticators of the\n        particular identity.')
ipsAuthCredentialAttributesEntry = MibTableRow((1, 3, 6, 1, 2, 1, 141, 1, 6, 1, 1), ).setIndexNames((0, "IPS-AUTH-MIB", "ipsAuthInstIndex"), (0, "IPS-AUTH-MIB", "ipsAuthIdentIndex"), (0, "IPS-AUTH-MIB", "ipsAuthCredIndex"))
if mibBuilder.loadTexts: ipsAuthCredentialAttributesEntry.setDescription('An entry (row) containing management information\n        applicable to a credential that verifies a user\n        identity within an authorization instance.\n\n\n\n        To provide complete information in this MIB for a credential,\n        the management station must not only create the row in this\n        table but must also create a row in another table, where the\n        other table is determined by the value of\n        ipsAuthCredAuthMethod, e.g., if ipsAuthCredAuthMethod has the\n        value ipsAuthMethodChap, a row must be created in the\n        ipsAuthCredChapAttributesTable.')
ipsAuthCredIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 6, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1,4294967295)))
if mibBuilder.loadTexts: ipsAuthCredIndex.setDescription('An arbitrary integer used to uniquely identify a\n        particular Credential instance within an instance\n        present on the node.\n        This index value must not be modified or reused by\n        an agent unless a reboot has occurred.  An agent\n        should attempt to keep this value persistent across\n        reboots.')
ipsAuthCredAuthMethod = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 6, 1, 1, 2), AutonomousType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthCredAuthMethod.setDescription('This object contains an OBJECT IDENTIFIER\n        that identifies the authentication method\n        used with this credential.\n\n        When a row is created in this table, a corresponding\n        row must be created by the management station\n        in a corresponding table specified by this value.\n\n        When a row is deleted from this table, the corresponding\n        row must be automatically deleted by the agent in\n        the corresponding table specified by this value.\n\n\n\n\n        If the value of this object is ipsAuthMethodNone, no\n        corresponding rows are created or deleted from other\n        tables.\n\n        Some standardized values for this object are defined\n        within the ipsAuthMethodTypes subtree.')
ipsAuthCredRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 6, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthCredRowStatus.setDescription("This field allows entries to be dynamically added and\n        removed from this table via SNMP.  When adding a row to\n        this table, all non-Index/RowStatus objects must be set.\n        Rows may be discarded using RowStatus.  The value of\n        ipsAuthCredAuthMethod must not be changed while this row\n        is 'active'.")
ipsAuthCredStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 6, 1, 1, 4), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthCredStorageType.setDescription("The storage type for all read-create objects in this row.\n         Rows in this table that were created through an external\n         process may have a storage type of readOnly or permanent.\n         Conceptual rows having the value 'permanent' need not\n         allow write access to any columnar objects in the row.")
ipsAuthCredChap = MibIdentifier((1, 3, 6, 1, 2, 1, 141, 1, 7))
ipsAuthCredChapAttributesTable = MibTable((1, 3, 6, 1, 2, 1, 141, 1, 7, 1), )
if mibBuilder.loadTexts: ipsAuthCredChapAttributesTable.setDescription("A list of CHAP attributes for credentials that\n        use ipsAuthMethodChap as their ipsAuthCredAuthMethod.\n\n        A row in this table can only exist when an instance of\n        the ipsAuthCredAuthMethod object exists (or is created\n\n\n\n        simultaneously) having the same instance identifiers\n        and a value of 'ipsAuthMethodChap'.")
ipsAuthCredChapAttributesEntry = MibTableRow((1, 3, 6, 1, 2, 1, 141, 1, 7, 1, 1), ).setIndexNames((0, "IPS-AUTH-MIB", "ipsAuthInstIndex"), (0, "IPS-AUTH-MIB", "ipsAuthIdentIndex"), (0, "IPS-AUTH-MIB", "ipsAuthCredIndex"))
if mibBuilder.loadTexts: ipsAuthCredChapAttributesEntry.setDescription('An entry (row) containing management information\n        applicable to a credential that uses\n        ipsAuthMethodChap as their ipsAuthCredAuthMethod.\n\n        When a row is created in ipsAuthCredentialAttributesTable\n        with ipsAuthCredAuthMethod = ipsAuthCredChap, the\n        management station must create a corresponding row\n        in this table.\n\n        When a row is deleted from ipsAuthCredentialAttributesTable\n        with ipsAuthCredAuthMethod = ipsAuthCredChap, the\n        agent must delete the corresponding row (if any) in\n        this table.')
ipsAuthCredChapUserName = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 7, 1, 1, 1), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthCredChapUserName.setDescription('A character string containing the CHAP user name for this\n        credential.')
ipsAuthCredChapRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 7, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthCredChapRowStatus.setDescription("This field allows entries to be dynamically added and\n        removed from this table via SNMP.  When adding a row to\n        this table, all non-Index/RowStatus objects must be set.\n        Rows may be discarded using RowStatus.  The value of\n        ipsAuthCredChapUserName may be changed while this row\n        is 'active'.")
ipsAuthCredChapStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 7, 1, 1, 3), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthCredChapStorageType.setDescription("The storage type for all read-create objects in this row.\n         Rows in this table that were created through an external\n         process may have a storage type of readOnly or permanent.\n         Conceptual rows having the value 'permanent' need not\n         allow write access to any columnar objects in the row.")
ipsAuthCredSrp = MibIdentifier((1, 3, 6, 1, 2, 1, 141, 1, 8))
ipsAuthCredSrpAttributesTable = MibTable((1, 3, 6, 1, 2, 1, 141, 1, 8, 1), )
if mibBuilder.loadTexts: ipsAuthCredSrpAttributesTable.setDescription("A list of SRP attributes for credentials that\n        use ipsAuthMethodSrp as its ipsAuthCredAuthMethod.\n\n        A row in this table can only exist when an instance of\n        the ipsAuthCredAuthMethod object exists (or is created\n        simultaneously) having the same instance identifiers\n        and a value of 'ipsAuthMethodSrp'.")
ipsAuthCredSrpAttributesEntry = MibTableRow((1, 3, 6, 1, 2, 1, 141, 1, 8, 1, 1), ).setIndexNames((0, "IPS-AUTH-MIB", "ipsAuthInstIndex"), (0, "IPS-AUTH-MIB", "ipsAuthIdentIndex"), (0, "IPS-AUTH-MIB", "ipsAuthCredIndex"))
if mibBuilder.loadTexts: ipsAuthCredSrpAttributesEntry.setDescription('An entry (row) containing management information\n        applicable to a credential that uses\n        ipsAuthMethodSrp as their ipsAuthCredAuthMethod.\n\n\n\n\n        When a row is created in ipsAuthCredentialAttributesTable\n        with ipsAuthCredAuthMethod = ipsAuthCredSrp, the\n        management station must create a corresponding row\n        in this table.\n\n        When a row is deleted from ipsAuthCredentialAttributesTable\n        with ipsAuthCredAuthMethod = ipsAuthCredSrp, the\n        agent must delete the corresponding row (if any) in\n        this table.')
ipsAuthCredSrpUserName = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 8, 1, 1, 1), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthCredSrpUserName.setDescription('A character string containing the SRP user name for this\n        credential.')
ipsAuthCredSrpRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 8, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthCredSrpRowStatus.setDescription("This field allows entries to be dynamically added and\n        removed from this table via SNMP.  When adding a row to\n        this table, all non-Index/RowStatus objects must be set.\n        Rows may be discarded using RowStatus.  The value of\n        ipsAuthCredSrpUserName may be changed while the status\n        of this row is 'active'.")
ipsAuthCredSrpStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 8, 1, 1, 3), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthCredSrpStorageType.setDescription("The storage type for all read-create objects in this row.\n         Rows in this table that were created through an external\n         process may have a storage type of readOnly or permanent.\n         Conceptual rows having the value 'permanent' need not\n         allow write access to any columnar objects in the row.")
ipsAuthCredKerberos = MibIdentifier((1, 3, 6, 1, 2, 1, 141, 1, 9))
ipsAuthCredKerbAttributesTable = MibTable((1, 3, 6, 1, 2, 1, 141, 1, 9, 1), )
if mibBuilder.loadTexts: ipsAuthCredKerbAttributesTable.setDescription("A list of Kerberos attributes for credentials that\n        use ipsAuthMethodKerberos as their ipsAuthCredAuthMethod.\n\n        A row in this table can only exist when an instance of\n        the ipsAuthCredAuthMethod object exists (or is created\n        simultaneously) having the same instance identifiers\n        and a value of 'ipsAuthMethodKerb'.")
ipsAuthCredKerbAttributesEntry = MibTableRow((1, 3, 6, 1, 2, 1, 141, 1, 9, 1, 1), ).setIndexNames((0, "IPS-AUTH-MIB", "ipsAuthInstIndex"), (0, "IPS-AUTH-MIB", "ipsAuthIdentIndex"), (0, "IPS-AUTH-MIB", "ipsAuthCredIndex"))
if mibBuilder.loadTexts: ipsAuthCredKerbAttributesEntry.setDescription('An entry (row) containing management information\n        applicable to a credential that uses\n        ipsAuthMethodKerberos as its ipsAuthCredAuthMethod.\n\n        When a row is created in ipsAuthCredentialAttributesTable\n        with ipsAuthCredAuthMethod = ipsAuthCredKerberos, the\n        management station must create a corresponding row\n        in this table.\n\n        When a row is deleted from ipsAuthCredentialAttributesTable\n        with ipsAuthCredAuthMethod = ipsAuthCredKerberos, the\n        agent must delete the corresponding row (if any) in\n        this table.')
ipsAuthCredKerbPrincipal = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 9, 1, 1, 1), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthCredKerbPrincipal.setDescription('A character string containing a Kerberos principal\n        for this credential.')
ipsAuthCredKerbRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 9, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthCredKerbRowStatus.setDescription("This field allows entries to be dynamically added and\n        removed from this table via SNMP.  When adding a row to\n        this table, all non-Index/RowStatus objects must be set.\n        Rows may be discarded using RowStatus.  The value of\n        ipsAuthCredKerbPrincipal may be changed while this row\n        is 'active'.")
ipsAuthCredKerbStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 9, 1, 1, 3), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthCredKerbStorageType.setDescription("The storage type for all read-create objects in this row.\n         Rows in this table that were created through an external\n         process may have a storage type of readOnly or permanent.\n         Conceptual rows having the value 'permanent' need not\n         allow write access to any columnar objects in the row.")
ipsAuthCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 141, 2, 1))
ipsAuthGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 141, 2, 2))
ipsAuthInstanceAttributesGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 141, 2, 2, 1)).setObjects(*(("IPS-AUTH-MIB", "ipsAuthInstDescr"), ("IPS-AUTH-MIB", "ipsAuthInstStorageType"),))
if mibBuilder.loadTexts: ipsAuthInstanceAttributesGroup.setDescription('A collection of objects providing information about\n        authorization instances.')
ipsAuthIdentAttributesGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 141, 2, 2, 2)).setObjects(*(("IPS-AUTH-MIB", "ipsAuthIdentDescription"), ("IPS-AUTH-MIB", "ipsAuthIdentRowStatus"), ("IPS-AUTH-MIB", "ipsAuthIdentStorageType"),))
if mibBuilder.loadTexts: ipsAuthIdentAttributesGroup.setDescription('A collection of objects providing information about\n        user identities within an authorization instance.')
ipsAuthIdentNameAttributesGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 141, 2, 2, 3)).setObjects(*(("IPS-AUTH-MIB", "ipsAuthIdentName"), ("IPS-AUTH-MIB", "ipsAuthIdentNameRowStatus"), ("IPS-AUTH-MIB", "ipsAuthIdentNameStorageType"),))
if mibBuilder.loadTexts: ipsAuthIdentNameAttributesGroup.setDescription('A collection of objects providing information about\n        user names within user identities within an authorization\n        instance.')
ipsAuthIdentAddrAttributesGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 141, 2, 2, 4)).setObjects(*(("IPS-AUTH-MIB", "ipsAuthIdentAddrType"), ("IPS-AUTH-MIB", "ipsAuthIdentAddrStart"), ("IPS-AUTH-MIB", "ipsAuthIdentAddrEnd"), ("IPS-AUTH-MIB", "ipsAuthIdentAddrRowStatus"), ("IPS-AUTH-MIB", "ipsAuthIdentAddrStorageType"),))
if mibBuilder.loadTexts: ipsAuthIdentAddrAttributesGroup.setDescription('A collection of objects providing information about\n        address ranges within user identities within an\n        authorization instance.')
ipsAuthIdentCredAttributesGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 141, 2, 2, 5)).setObjects(*(("IPS-AUTH-MIB", "ipsAuthCredAuthMethod"), ("IPS-AUTH-MIB", "ipsAuthCredRowStatus"), ("IPS-AUTH-MIB", "ipsAuthCredStorageType"),))
if mibBuilder.loadTexts: ipsAuthIdentCredAttributesGroup.setDescription('A collection of objects providing information about\n        credentials within user identities within an authorization\n        instance.')
ipsAuthIdentChapAttrGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 141, 2, 2, 6)).setObjects(*(("IPS-AUTH-MIB", "ipsAuthCredChapUserName"), ("IPS-AUTH-MIB", "ipsAuthCredChapRowStatus"), ("IPS-AUTH-MIB", "ipsAuthCredChapStorageType"),))
if mibBuilder.loadTexts: ipsAuthIdentChapAttrGroup.setDescription('A collection of objects providing information about\n        CHAP credentials within user identities within an\n        authorization instance.')
ipsAuthIdentSrpAttrGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 141, 2, 2, 7)).setObjects(*(("IPS-AUTH-MIB", "ipsAuthCredSrpUserName"), ("IPS-AUTH-MIB", "ipsAuthCredSrpRowStatus"), ("IPS-AUTH-MIB", "ipsAuthCredSrpStorageType"),))
if mibBuilder.loadTexts: ipsAuthIdentSrpAttrGroup.setDescription('A collection of objects providing information about\n        SRP credentials within user identities within an\n        authorization instance.')
ipsAuthIdentKerberosAttrGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 141, 2, 2, 8)).setObjects(*(("IPS-AUTH-MIB", "ipsAuthCredKerbPrincipal"), ("IPS-AUTH-MIB", "ipsAuthCredKerbRowStatus"), ("IPS-AUTH-MIB", "ipsAuthCredKerbStorageType"),))
if mibBuilder.loadTexts: ipsAuthIdentKerberosAttrGroup.setDescription('A collection of objects providing information about\n        Kerberos credentials within user identities within an\n        authorization instance.')
ipsAuthComplianceV1 = ModuleCompliance((1, 3, 6, 1, 2, 1, 141, 2, 1, 1)).setObjects(*(("IPS-AUTH-MIB", "ipsAuthInstanceAttributesGroup"), ("IPS-AUTH-MIB", "ipsAuthIdentAttributesGroup"), ("IPS-AUTH-MIB", "ipsAuthIdentNameAttributesGroup"), ("IPS-AUTH-MIB", "ipsAuthIdentAddrAttributesGroup"), ("IPS-AUTH-MIB", "ipsAuthIdentCredAttributesGroup"), ("IPS-AUTH-MIB", "ipsAuthIdentChapAttrGroup"), ("IPS-AUTH-MIB", "ipsAuthIdentSrpAttrGroup"), ("IPS-AUTH-MIB", "ipsAuthIdentKerberosAttrGroup"),))
if mibBuilder.loadTexts: ipsAuthComplianceV1.setDescription('Initial version of compliance statement based on\n        initial version of this MIB module.\n\n        The Instance and Identity groups are mandatory;\n        at least one of the other groups (Name, Address,\n        Credential, Certificate) is also mandatory for\n        any given implementation.')
mibBuilder.exportSymbols("IPS-AUTH-MIB", ipsAuthIdentAddrRowStatus=ipsAuthIdentAddrRowStatus, ipsAuthIdentAddrAttributesEntry=ipsAuthIdentAddrAttributesEntry, ipsAuthCompliances=ipsAuthCompliances, ipsAuthMibModule=ipsAuthMibModule, ipsAuthCredKerbPrincipal=ipsAuthCredKerbPrincipal, ipsAuthCredSrpRowStatus=ipsAuthCredSrpRowStatus, ipsAuthCredSrp=ipsAuthCredSrp, ipsAuthMethodKerberos=ipsAuthMethodKerberos, ipsAuthIdentNameAttributesGroup=ipsAuthIdentNameAttributesGroup, ipsAuthIdentIndex=ipsAuthIdentIndex, ipsAuthInstDescr=ipsAuthInstDescr, ipsAuthCredChapAttributesTable=ipsAuthCredChapAttributesTable, ipsAuthIdentStorageType=ipsAuthIdentStorageType, ipsAuthIdentSrpAttrGroup=ipsAuthIdentSrpAttrGroup, ipsAuthCredSrpAttributesEntry=ipsAuthCredSrpAttributesEntry, ipsAuthIdentNameAttributesEntry=ipsAuthIdentNameAttributesEntry, ipsAuthIdentAddrStart=ipsAuthIdentAddrStart, ipsAuthNotifications=ipsAuthNotifications, ipsAuthIdentNameIndex=ipsAuthIdentNameIndex, ipsAuthIdentityName=ipsAuthIdentityName, ipsAuthIdentAttributesEntry=ipsAuthIdentAttributesEntry, ipsAuthIdentAddrIndex=ipsAuthIdentAddrIndex, ipsAuthCredSrpStorageType=ipsAuthCredSrpStorageType, ipsAuthIdentAttributesTable=ipsAuthIdentAttributesTable, ipsAuthIdentNameRowStatus=ipsAuthIdentNameRowStatus, ipsAuthCredIndex=ipsAuthCredIndex, ipsAuthCredKerbAttributesEntry=ipsAuthCredKerbAttributesEntry, ipsAuthIdentAddrType=ipsAuthIdentAddrType, ipsAuthCredKerbRowStatus=ipsAuthCredKerbRowStatus, ipsAuthInstIndex=ipsAuthInstIndex, ipsAuthDescriptors=ipsAuthDescriptors, ipsAuthIdentKerberosAttrGroup=ipsAuthIdentKerberosAttrGroup, ipsAuthCredKerberos=ipsAuthCredKerberos, ipsAuthConformance=ipsAuthConformance, ipsAuthInstanceAttributesEntry=ipsAuthInstanceAttributesEntry, ipsAuthMethodTypes=ipsAuthMethodTypes, ipsAuthIdentChapAttrGroup=ipsAuthIdentChapAttrGroup, ipsAuthInstStorageType=ipsAuthInstStorageType, ipsAuthCredChap=ipsAuthCredChap, ipsAuthIdentAddrAttributesGroup=ipsAuthIdentAddrAttributesGroup, ipsAuthInstance=ipsAuthInstance, ipsAuthIdentNameStorageType=ipsAuthIdentNameStorageType, ipsAuthIdentRowStatus=ipsAuthIdentRowStatus, ipsAuthIdentityAddress=ipsAuthIdentityAddress, ipsAuthIdentDescription=ipsAuthIdentDescription, ipsAuthCredential=ipsAuthCredential, ipsAuthComplianceV1=ipsAuthComplianceV1, ipsAuthCredentialAttributesEntry=ipsAuthCredentialAttributesEntry, ipsAuthGroups=ipsAuthGroups, ipsAuthCredKerbAttributesTable=ipsAuthCredKerbAttributesTable, ipsAuthCredSrpAttributesTable=ipsAuthCredSrpAttributesTable, ipsAuthCredChapUserName=ipsAuthCredChapUserName, ipsAuthIdentName=ipsAuthIdentName, ipsAuthIdentCredAttributesGroup=ipsAuthIdentCredAttributesGroup, ipsAuthIdentity=ipsAuthIdentity, IpsAuthAddress=IpsAuthAddress, ipsAuthObjects=ipsAuthObjects, ipsAuthIdentAddrAttributesTable=ipsAuthIdentAddrAttributesTable, ipsAuthIdentAddrStorageType=ipsAuthIdentAddrStorageType, ipsAuthCredRowStatus=ipsAuthCredRowStatus, ipsAuthCredChapRowStatus=ipsAuthCredChapRowStatus, ipsAuthMethodNone=ipsAuthMethodNone, ipsAuthCredChapStorageType=ipsAuthCredChapStorageType, ipsAuthCredSrpUserName=ipsAuthCredSrpUserName, ipsAuthInstanceAttributesGroup=ipsAuthInstanceAttributesGroup, ipsAuthIdentAddrEnd=ipsAuthIdentAddrEnd, ipsAuthCredAuthMethod=ipsAuthCredAuthMethod, ipsAuthCredStorageType=ipsAuthCredStorageType, ipsAuthCredentialAttributesTable=ipsAuthCredentialAttributesTable, ipsAuthCredChapAttributesEntry=ipsAuthCredChapAttributesEntry, ipsAuthMethodSrp=ipsAuthMethodSrp, ipsAuthIdentNameAttributesTable=ipsAuthIdentNameAttributesTable, ipsAuthCredKerbStorageType=ipsAuthCredKerbStorageType, ipsAuthInstanceAttributesTable=ipsAuthInstanceAttributesTable, ipsAuthMethodChap=ipsAuthMethodChap, PYSNMP_MODULE_ID=ipsAuthMibModule, ipsAuthIdentAttributesGroup=ipsAuthIdentAttributesGroup)