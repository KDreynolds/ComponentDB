/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package gov.anl.aps.cms.portal.model.entities;

import java.io.Serializable;
import java.util.List;
import javax.persistence.Basic;
import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.NamedQueries;
import javax.persistence.NamedQuery;
import javax.persistence.OneToMany;
import javax.persistence.Table;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.Size;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlTransient;

/**
 *
 * @author sveseli
 */
@Entity
@Table(name = "setting_type")
@XmlRootElement
@NamedQueries({
    @NamedQuery(name = "SettingType.findAll", query = "SELECT s FROM SettingType s"),
    @NamedQuery(name = "SettingType.findById", query = "SELECT s FROM SettingType s WHERE s.id = :id"),
    @NamedQuery(name = "SettingType.findByName", query = "SELECT s FROM SettingType s WHERE s.name = :name"),
    @NamedQuery(name = "SettingType.findByDescription", query = "SELECT s FROM SettingType s WHERE s.description = :description"),
    @NamedQuery(name = "SettingType.findByDefaultValue", query = "SELECT s FROM SettingType s WHERE s.defaultValue = :defaultValue")})

public class SettingType implements Serializable
{
    private static final long serialVersionUID = 1L;
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Basic(optional = false)
    @Column(name = "id")
    private Integer id;
    @Basic(optional = false)
    @NotNull
    @Size(min = 1, max = 128)
    @Column(name = "name")
    private String name;
    @Size(max = 256)
    @Column(name = "description")
    private String description;
    @Size(max = 64)
    @Column(name = "default_value")
    private String defaultValue;
    @OneToMany(cascade = CascadeType.ALL, mappedBy = "settingType")
    private List<UserSetting> userSettingList;

    public SettingType() {
    }

    public SettingType(Integer id) {
        this.id = id;
    }

    public SettingType(Integer id, String name) {
        this.id = id;
        this.name = name;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public String getDefaultValue() {
        return defaultValue;
    }

    public void setDefaultValue(String defaultValue) {
        this.defaultValue = defaultValue;
    }

    @XmlTransient
    public List<UserSetting> getUserSettingList() {
        return userSettingList;
    }

    public void setUserSettingList(List<UserSetting> userSettingList) {
        this.userSettingList = userSettingList;
    }

    @Override
    public int hashCode() {
        int hash = 0;
        hash += (id != null ? id.hashCode() : 0);
        return hash;
    }

    @Override
    public boolean equals(Object object) {
        // TODO: Warning - this method won't work in the case the id fields are not set
        if (!(object instanceof SettingType)) {
            return false;
        }
        SettingType other = (SettingType) object;
        return (this.id != null || other.id == null) && (this.id == null || this.id.equals(other.id));
    }

    @Override
    public String toString() {
        return "gov.anl.aps.cms.test.entities.SettingType[ id=" + id + " ]";
    }
    
}
